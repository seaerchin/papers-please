# Introduction 
- modern transaction processing workloads are becoming increasingly *geo-distributed*
	- data must reside close to users to provide low latency (eg: edge computing)
	- *personal* data should adhere to local laws (eg: for EU citizens, stay within EU)
- cockroachDB aims to support the following technical features 
	1. fault tolerance and high availability -> CRDB (cockroachDB) maintains three replicas of every partition in DB across geographica zones 
	2. geo-distributed partitioning and replica placement -> CRDB is horizontally scalable and adds capacity as required 
	3. high performance transactions -> CRDB's transaction protocol supports performant geo-distrbuted transactions. this allows for *serializable isolation* without specialized hardware. 

# System Overview 
## Architecture of CockroachDB
- [shared nothing architecture](https://en.wikipedia.org/wiki/Shared-nothing_architecture)-> all nodes are used for both data storage and computation but each request is only satisfied by a **single node**
	- nodes can be within single data center or spread around the globe -> this seems to imply leaderless replication -> how to lower partitioning rates? (see [[CAP 12 years later#CAP latency connection | section on latency]])
	- Ranges are satisfied by a node (not 1:1) -> Each range will always be served by the same RAFT group
- [CRDB](**https://www.youtube.com/watch?v=OJySfiMKXLs**) consists of **three** layers as follows

1. SQL ->  this is the interface for all user interactions with the database. Includes SQL parser, optimizer and execution engine.
	- this converts SQL statements into r/w requests to the underlying K/V store
	- the SQL layer is *unaware* of how data is actually partitioned or distributed -> this is because. the underlying layer present a K/V store as an abstraction
2. Transactional K/V -> ensures *atomicity* of changes spanning multiple KV pairs
	- This is also responsible for CRDB's isolation guarantees
	- Consistency and Isolation is handled by RAFT at the *range* level but the SQL level could have a higher level of expressiveness -> eg: table A consists of ranges [1, 3]
		- this acts as an intermediary between the ranges and the SQL level
3. Distribution -> presents an abstraction of *monolithic logical key space ordered by key* 
	- this implies that all data is addressable by key
	- CRDB uses *range partitioning* on the keys to divide data into 64MB of contiguous ordered chunks 

### Ranges
- 64MB chosen as a sweet spot as it's small enough to easily shift between nodes but large enough to store contiguous set of data liekly to be accessed together 
- Ranges start empty, split when too large and merge when too small (ie, rebalancing)
	- when rebalancing from old -> new, the new range will always get *more* data (ie new' > new) 
	- even when old or new goes down, we can reboot and retry until new signals that the rebalancing is done 
- Ranges also split based on load to reduce hotspots and cpu usage imbalances
- each range is replicated 3x w/ each copy on diff node -> ensures durability of modifications using consensus-based replication

## Fault tolerance and high availability
- A is guaranteed through 3 measures
	- replication of data 
	- automatic recovery (when fail) 
	- strategic data placement 

### Replication using RAFT 
- Each range is partitioned 3-ways and they form a *RAFT group*, where there is 1 leader and 2 followers 
- The unit of replication in CRDB is a *command* 
	- *definition:* a command is a *sequence of low-level edits* to be made to the storage engine
- RAFT maintains a consistent, ordered log of updates across replicas and each replica applies update when RAFT declares it as *committed*
- CRDB uses range-level *leases*, where a replica (usually the RAFT leader) acts as the *leaseholder*. 
	- This makes it the **only** replica allowed to serve authoritative **up-to-date** reads or propose writes to the leader. 
	- when would the leaseholder **not** be the leader? 

> as writes go through the leaseholder, reads can bypass networking round trips required by RAFT without sacrificing consistency

**what does this mean?** 
*Guess*: if we serve reads from the **leaseholder** then all reads will naturally be up-to-date and "consistent".  

However, consider the following scenario: 
- Leaseholder (LH) serves read 1
- client writes to LH
- LH dies before write can be broadcasted -> only Leader (L) + 1 other node remains, without write 
- client reads -> served by L, when recover, network will be missing the write **unless** the write is propagated (but then we will already be inconsistent with the current read)

*Ans*: this isn't true -> writes have to be acknowledged (as per RAFT); only reads don't so in this scnenario, L will still see the write.

**Question**: how does CRDB prevent us from seeing inconsistent reads when LH != L and LH goes down?
*Ans*: when LH goes down, CRDB attempts to elect another LH', which will then serve reads -> this is no longer inconsistent as LH' will serve 

[How leases are transferred from a dead node](https://www.cockroachlabs.com/docs/stable/architecture/replication-layer.html)
- LH1 goes down - (4.5s passes) -> heartbeat not ACKed -> follower tries to acquire lease -> rejected as only L can acquire -> (if L goes down, elect L' else L takes over as LH) -> LH2 established -> write to DB and broadcast to network -> LH1 joins back but knows that cannot be LH as LH2 with version of 2 > 1 
	- prior to LH2 acquiring a lease, it needs to include LH1's lease when requesting for the new lease. 

### Membership changes and automatic load rebalancing 
- short term failures use RAFT to failover

> For longer-term failures, CRDB automatically creates new replicas of under-replicated Ranges

- ^ the above seems to imply that a long term failure will cause the RAFT group (of 3 nodes) to operate as a master-slave config (1-1) 
	- what counts as "long-term failure"? if i have a node dropping ~70% of requests but responds to heartbeat, does that count?
- overseer (possibly co-ordinator) assigns a node to the range group that has the failure 
	- the RAFT leader then initiates the catchup process

### Replica placement
- 2 parts - user/automatic
	- user can determine through node locality (eg: country) or capability (eg: RAM -> maybe only US-E has it)
	- automatic done through spreading replicas across failure domains (eg: rack | center | geographic) 

## Data Placement Policies
- **geo-partitioned replica**: high # of req from specific location + latency is a concern
	- fast intra-region reads + writes but if that AZ goes down, this means a widespread failure for data specific to that region 
- **geo-partitioned leaseholders**: can survive AZ going down but slow to write (reads can go through the lease-holder so it's still fast)
- **duplicated indexes**: write amplification (1 write might potentially alter b-tree structure underneath + this needs to be duplicated across indexes) + slower cross-region writes but useful when data is **infrequently updated** + geographically distrtibuted
	- note that leaseholders are still pinned to the region

# Transactions
- a transaction can span the **entire** key-space.
	- does this means that eg: W1 (v2) -> R1, R1 will have to read stale (v < 2 = 1) data to avoid latency?
	- logical seq: R1 -> W1 as version of R1 is 1 and version of W1 is 2 
- CRDB uses *multi-version concurrency control* (MVCC)to provide *serialization isolation*
		- [serializable isolation](https://www.postgresql.org/docs/current/transaction-iso.html#XACT-SERIALIZABLE) is the guarantee that all events to the database can be seen as a **linear** sequence of events 

## Overview
- a transaction starts at the *gateway* node. This node co-ordinates requests between client and db.

### Execution at xact co-ord
- sql requires that response to current op must be returned before next op can be issued. 
	- hence, to avoid stalling while ops are replicated, co-ordinator uses 2 optimizations: *write pipelining* and *parallel commits*

- *Write pipelining* allows for returning a result w/o waiting for the replication of the current operation 
		- **Question**: how can this be durable then? eg: if i write x = 1 and i don't replicate, it is entirely possible that eg: Leader crashes -> Replicas become new leader -> old leader recovers and becomes replica -> ??? 
	- *Ans:* TODO (probably related to RAFT failover, section on logs)

- *Parallel commits* let the commit op + write pipeline replicate in parallel

- Allows multi statement SQL xact to complete w/ latency of single round replication 
	- presumably, LH keeps broadcasting commit ops with last ACK-ed op as starting?

#### Write pipelining
- operation can always be executed if it does not depends on any earlier operation 
	- similar to CPU pipelining 
- hence, unrelated operation can keep on being pipelined and avoid stalling execution

#### Parallel commits
- establishes a *staging* state (super-position of committed/aborted) that is dependent on all its writes being replicated 
- co-ordinator can then establish + replicate the staging status while replicating writes *in parallel* -> less time wasted on sequencing writes

NOTE: reader is referring to L2 -> the K/V overseeing the ranges 

### Execution at the leaseholder

## Atomicity Guarantees
- all writes are *provisional* (ie, subject to change) until commit time -> such provisional writes are called *write intents*

*definition (write intents)*: A write intent is a regular MVCC kv pair except that it has meta-data at the start indicating that it is an intent. 
	- this metadata points to a *transaction record*, which is a special key (unique per xact) that stores the current state of the xact (`pending | staging | committed | aborted`)

- readers (presumably higher layer) will 
	- abort if intent is *staging*
	- block if intent is *pending* 
	- read if intent is *committed*
	- ignore if intent is *aborted*

## Concurrency control 
**note**: read here refers to db reads 

### write-read conflicts
- a read running into a **uncommitted** intent w/ lower timestamp (ie, arrived earlier) will wait (as intent is *staging*/*pending*)
	- if the timestamp is higher, the read is logically first and can avoid the wait

### read-write conflicts
- a write cannot proceed if there is some read with a higher timestamp at the same key. this is because the read has already seen the currently existing value 
	- eg: read sees (x = 1 -> x  3) with t = 2 
	- then write of (x = 1 -> x = 2) comes in with t = 1 
	- client alr sees x = 3 at t  = 2 so if the write is allowed to proceed with t = 1, the client's state would be invalid -> at t = 2, x = 1 -> x = 3 but at t = 1, x = 1 -> x = 2 implying that x = 1 was not a valid state at t = 2

### write-write conflicts 
- write running into an uncomitted intent w/ lower timestamp will wait
- write running into a *committed* value at a higher timestamp (for same key) will advance its own timestamp past it

## Read refreshes
- idea is that we can advance if no data read in the xact at t = a has been updated in the interval (a, b]
- CRDB maintains a set of keys in this xact's *read set*. a *read refresh* request validates that the set of keys have not been updated in a given interval (fulfilling the condition above), which allows timestamp advancement 
	- this is essentially scanning the read set and checking if any MVCC values fall in the given interval
- once xact reads something, that key is put into the xact's read set 
- next, when crdb wants to do a read refresh, it check's the xact's read set and scans the values for the version number to determine if any in interval 
- Advacning a xact's read timestamp is also required when a scan encounters an *uncertain* value that could be in either the reader's past or future  

## Follower reads 
- non-LH replicas can serve requests for **read-only** queries with timestamps sufficiently in the past 
	- done through special `AS OF SYSTEM TIME` query modifier 
- to achieve this, the replica needs to know that *no future writes can invalidate the read retroactively* (see [[#read-write conflicts]])
	- LH cannot serve any writes with T (write) <= T (read) 
	- follower must also have caught up to prefix of the RAFT log affecting the MVCC snapshot at T (data required for read is up-to-date w/o possible modifications) 

> Closed timestamps, alongside Raft log indexes at the time, are exchanged periodically between replicas 

^ seems to imply a gossip protocol, which might potentially introduce inter-network latency?  ^4bd32c

*definition (closed timestamp):* The timestamp below which, no further writes will be accepted.
	- this means that writes will only go through if t (write) >= latest closed timestamp

> Follower replicas use the state built up from received updates to determine if they have all the data needed to serve consistent reads at a given timestamp

**question:** what happens if crdb floods the nework -> then t = 3 should be closed but follower doesn't receive it and serves a read request?
*answer:* should still be ok? follower cannot serve a read-request without having knowledge of the closed timestamp anyway

- nodes keep a record of their latency (ie, a fully-connected graph w/ edge weights = latency) w/ every other node
	- when a node receives a read request w/ sufficiently old timestamp, it will forward the request to the closest node (lowest latency) w/ replica of data (possibly itself)

# Clock synchronization 
- uses a hybrid logical clock scheme for timestamp ordering
	- allows for loosely synced clocks to provide single-key linearizability between transactions 

## Hybrid logical clocks (HLC)
- this HLC provides a timestamp formed by a combination of physical and logical time 
- HLCs within crdb deployment are configured with a **maximum allowable offset** between their physical time and that of other HLCs in the system
	- this is to migitate [*clock drift*](https://en.wikipedia.org/wiki/Clock_drift)

### Properties provided by HLCs
#### Causality tracking
- *causality tracking* is provided through their **logical** component upon each inter-node exchange ([[#^4bd32c | gossip protocol]] mentioned earlier)
	- nodes attach HLC timestamps to each message sent and use HLC timestamps from messages received to update their local clock

> Capturing causal relationships between events on different nodes is critical for enforcing invariants within CRDB. The most important of these is a lease disjointness invariant similar to that in Spanner: for each Range, each lease interval is disjoint from every other lease interval

^ paper says that "This is enforced on cooperative lease handoff with causality transfer through the HLC" 
	- **question:** what does that even mean?
	- *answer:* causality transfer is using the maximum allowable offset so that the logical + physical clocks will always reflect this handoff

#### Strict monotonicity within/across restarts
- is this referring to timestamp allocation (?)
- trivial for continuous process
- across restarts, wait out the maximum clock offset (500ms) before serving requests
	- since the process has waited out max offset, it will always see another request w/ timestamps coming in and can use that timestamp
- ensures that two causally depenent xacts from same node will always have timestamps that reflect their real time ordering

#### Self-stabilization
- HLCs provide self-stabilization in the presence of **isolated transient** clock skew fluctuations
- Due to [[#^4bd32c | gossip protocol]], HLCs across node will tend to converge to a stable value