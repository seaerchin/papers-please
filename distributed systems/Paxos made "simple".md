
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

however, this might result in deadlock: 
- several proposers can propose values -> consider 3 proposers, if we have [n, n, 1], we have gridlock. 

hence, this implies that

> **Requirement**
> An acceptor must be allowed to accept >=1 proposal

and also, that a proposal will be tracked by assigning a positive integer to it, so that a proposal consists of (value, tracking integer). 

this implies that a value is only chosen **when a single proposal with that value has been accepted by a majority of the acceptors**