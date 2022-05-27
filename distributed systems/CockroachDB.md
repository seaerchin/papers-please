# Introduction 
- modern transaction processing workloads are becoming increasingly *geo-distributed*
	- data must reside close to users to provide low latency (eg: edge computing)
	- *personal* data should adhere to local laws (eg: for EU citizens, stay within EU)
- cockroachDB aims to support the following technical features 
	1. fault tolerance and high availability -> CRDB (cockroachDB) maintains three replicas of every partition in DB across geographica zones 
	2. geo-distributed partitioning and replica placement -> CRDB is horizontally scalable and adds capacity as required 
	3. high performance transactions -> CRDB's transaction protocol supports performant geo-distrbuted transactions. this allows for *serializable isolatin* without specialized hardware. 

# System Overview 
## Architecture of CockroachDB
- *[shared nothing architecture](https://en.wikipedia.org/wiki/Shared-nothing_architecture#:~:text=A%20shared-nothing%20architecture%20(SN,the%20same%20memory%20or%20storage.)* -> all nodes are used for both data storage and computation but each request is only satisfied by a **single node**
	- nodes can be within single data center or spread around the globe -> this seems to imply leaderless replication -> how to lower partitioning rates? (see [[CAP 12 years later#CAP latency connection | section on latency]])
- CRDB consists of **three** layers as follows

1. SQL ->  this is the interface for all user interactions with the database. Includes SQL parser, optimizer and execution engine.
	- this converts SQL statements into r/w requests to the underlying K/V store
	- the SQL layer is *unaware* of how data is actually partitioned or distributed -> this is because. the underlying layer present a K/V store as an abstraction
2. Transactional K/V -> ensures *atomicity* of changes spanning multiple KV pairs
	- This is also responsible for CRDB's isolation guarantees
3. Distribution -> presents an abstraction of *monolithic logical key space ordered by key* 
	- this implies that all data is addressable by key
	- CRDB uses *range partitioning* on the keys to divide data into 64MB of contiguous ordered chunks 

### Ranges
- 64MB chosen as a sweet spot as it's small enough to easily shift between nodes but large enough to store contiguous set of data liekly to be accessed together 
- Ranges start empty, split when too large and merge when too small (ie, rebalancing)
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