# Formal Model

## Atomic Data Objects

^fef87a

*definition*: atomicity/linearizable consistency is the guarantee that there is a *total order* on operations such that each operation looks like it's completed in a single instance
 $\quad$  - equivalent to requiring the distributed shared memory act like it belongs to a single node. 

## Available Data Objects

^0aeaee
**(what is an object?)**

*definition*: to be continuously available, **every** request received must result in a response
$\quad$   - this is equivalent to every request being serviced -> no infinite loops

### Partition Tolerance
- to model partition tolerance, the network must be allowed to lose an arbitrary amount of messages. 
  - when this happens, all messages from nodes in partition A to nodes in partitions B are lost. (the partitions are *disjoint*)
- by our definition of [[#^fef87a | atomicity]], this implies that even when some messages to the network is lost, the responses are still linear
  - x = 1 (this fails on some nodes) -> x = 2 -> x = 1 will never be read after
  - B gets delivered
  - A' gets retried and is successful
  - the sequence of events would not be A -> B -> A' but would be A -> B
- by our definition of [[#^0aeaee | availability]], *every* node that receives a request **must** respond
  - if we relax this requirement to allow 1 single node to not respond, the client might be stuck in an infinite loop as follows: 
  - client sends message A 
  - network gets partitioned into (N, M) where |N| = 1
  - message goes to N
  - N is allowed to not respond -> client receives no response even when network is functional 

# Asynchronous Networks
*definition*: there is no clock and nodes make decision based on messages received and local computation ^97b4ee

## Impossibility Result
**Theorem 1:** *It is impossible in an async network model to implement a r/w data object that has both availability and atomic consistency*

*Proof*: Assume some algorithm A exists that provides availability, atomic consistency and partition tolerance. Let N be our network and {N1, N2} be the disjoint sets of N.

Assume some write occurs to N1 and some read occurs to N2. It is impossible for the read to N2 to read the prior write to N1 as the sets are disjoint. 

**Collorary:** *It is impossible in an async network model to implement a r/w data object that has both availability and atomic consistency **when no messages are lost***

*Proof*: By our [[#^97b4ee | definition]] of an async network, nodes have no way to determine if a message has been lost or otherwise delayed (no clock). Hence, if an algo to guarantee atomic consistency when no messages have been lost exist, it can be extended to the general case where messages are lost **(need clarification on this)**

## Solutions in Async model 
we can achieve any 2/3 of the properties: 

#### Atomic, Partition Tolerant
- trivial: ignore every request 
- stronger: if all messages delivered, the network is available and terminates. 
- a centralised algo meets this criterion: we force the client to go through some node N, so even if partition, it will still be atomic (other partition without N will not be available)

#### Atomic, Available
- same, centralised algo 

#### Available, Partition Tolerant
- trivial: return initial value on every subsequent read 

# Partially synchronous networks
## Partially sychronous model 
*definition*: similar to [[#^97b4ee|definition]] of async networks but nodes are allowed to have local clocks.

