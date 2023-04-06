
## The consensus algorithm
### The problem
If a collection of processes can propose values, then a consensus algo should maintain the following invariants: 
	- only a _proposed_ value may be chosen 
	- only a _single_ value may be chosen 
	- processes should be able to learn the chosen value
	- a process never learns that a value has been chosen unless it actually has been 

note that this has no precise liveness requirements (ie, no specifications on how to avoid deadlock/that progress is always made); however, goal is to ensure that _some_ value is eventually chosen, and that once chosen, processes can be made aware of that value _eventually_

3 roles (of agents) in our consensus model 
- proposers 
- acceptors 
- learners 
the model that we operate in is the standard byzantine model, in which: 
- agents operate at arbitrary speed, may fail by stopping and may restart. an important property here is that *all* agents may fail by stopping and hence, a solution is impossible unless some information can be remembered by an agent that has failed and restarted. 
- messages can take arbitrarily long to be delivered, can be duplicated and can be lost but they are not corrupted.

### choosing a value  
- just have a single *acceptor agent* 
	- proposer -> acceptor 
	- this model means that if the acceptor fails, no new value can be chosen
- alternative: have multiple acceptor agents (N is odd) 
	- proposer -> acceptors -> if n > N//2 accept, value is chosen 

In absence of message loss or failure (ie, happy path), we want a value to be chosen even if **only 1 value is proposed by 1 proposer**, which suggests the following requirement: 

> **Requirement**
> P1: An acceptor **must** accept the first proposal it receives

otherwise, an acceptor (worst case: only 1) in the above case can wait for the second value, which results in no value being chosen (violation as there is valid proposal)
- however, this **does not** mean that the acceptor cannot change its value
- it can accept -> change 

however, this might result in deadlock: 
- several proposers can propose values -> consider 3 proposers, if we have [n, n, 1], we have gridlock. 

hence, this implies that

> **Requirement**
> An acceptor must be allowed to accept >=1 proposal

and also, that a proposal will be tracked by assigning a positive integer to it, so that a proposal consists of (value, tracking integer). 

this implies that a value is only chosen **when a single proposal with that value has been accepted by a majority of the acceptors**.

Because we allow multiple proposals to be chosen, we must guarantee that **all chosen proposals have the same value**.
	- **Q:** why allow multiple proposals to be chosen?
	- ie, for any tuple of (value, tracking integer), all `v in value` **must be the same** (value is a set of size 1)

As we want to allow multiple proposals to be chosen, we must guarantee the following invariant: 

> [!NOTE] Requirement
> P2: If a proposal with value *v* is chosen, **all** higher numbered proposal that is chosen has value *v*

This guarantees safety (so that all chosen proposals have same value). 

To be chosen, a value has to be accepted. Hence, we can satisfy P2 by satisfying P2a: 


> [!NOTE] Requirement
> P2a: If a proposal with value *v* is chosen, then **all** higher numbered proposal accepted by **any** accepter has value *v*

However, P2a could be violated under an async communication model together with P1. Consider the following: 
1. Quorum size = 3 (a, b, c)
2. a, b accept `(v = 1, n = 1)` 
3. c does not receive anything
4. proposer wakes and proposes `(v = 2, n = 2)`
5. due to P1, c accepts `(v = 2, n = 2)`, violating P2a.
6. c receives `(v = 1, n = 1)`

To satisfy P1 and P2a, we must strenghten P2a to: 

> [!NOTE] Requirement
> P2b: If a proposal with value *v* is chosen, then every higher-numbered proposal issued by any proposer has value *v*.
