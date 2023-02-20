
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