# why 2 out of 3 is misleading

- partitioning is not guaranteed -> partitions rarely happens and when they are **not** present in the system, there is little incentive to forfeit either C || A 
- choice between C || A can happen many times in the system at *differing levels of granularity* -> subsystems are allowed to make diff choices for C || A and it can vary based on many factors 
- C || A is **not** a binary choice (eg: if C is chosen then forfeits A) but more of a sliding scale -> eg: if strong consistency is the guarantee offered under C then A cannot be "always available"

- as the paper notes, 

> choosing CA should mean that the probability of a partition is far less than that of other systemic failures, such as disasters or multiple simultaneous faults.

which seems to imply that CA should only be chosen when the probability of other failures >> partition risk (what's the failover strategy in this case?)

# CAP latency connection
## partition decision
- during a timeout, a program must always make a *partition decision*: 
	- *cancel* operation and thus preserve C but forfeits A 
	- *proceed* operation and thus preserves A but forfeits C 
- retrying the communication does not solve the problem but simply delays the choice - even if current retry fails, there's no guarantee that next one will succeed. at some point, the program will have to make the decision 
- hence, a partition is a *time bound on communication* -> failure to achieve consistency within this time bound thus implies a partition

**Collorary 1**: There is no global notion of a partition
*Proof*: consider 2 nodes (A, B) that are part of a system. Assume that A has time-out of 1s and B never -> A will assume partition if request takes 2s but B will see that it succeeded.  ^ac31ec

**Collorary 2**: Nodes can enter a *partition mode* 
*Proof*: From [[#^ac31ec| Collorary 1]], when A detects a timeout, A assumes a partition and can take certain measures to circumvent 

****