# Introduction

## Definitions

**State machine**: a collection of states, transitions and the current state (basically a graph)
	- a transition to a new current state happens in response to an *issued operation* and **produces an output**
	- we allow self transitions; this is used to model *read-only operations*
	- in a *deterministic state machine*, for any `(state, operation)`, the transition enabled by the operation is **unique** and `output = f(state, operation)`
		- what does uniqueness imply here

**Asynchronous environment**: no bounds on timing. anything can take infinitely long

**Crash failure**: no more transitions possible and current state will persist indefinitely
	- in a *fail stop* environment, crash failures can be reliably detected. but in an *async environment*, an external observer cannot tell if another machine has crashed or is just extremely slow

**State machine replication**: collection of replicas of a particular **deterministic state machine**
	- because it is deterministic, giving the same input values would result in correct output
	- assumption: **at least 1 replica never crashed but we do not know, a priori, which replica this is.**

# How and why paxos works
- leaders + acceptors 

## clients, replicas, slots and configurations
- tolerate *f* crashes, paxos needs f + 1 replicas to maintain copies of the application state
- when client wants to execute a command `c = (k. cid, op)`, it broadcasts a `(request, c)` message to all replicas and waits for `(response, cid, result)` message from **one** of the replicas
- replicas can be thouhgt of as having a sequence of *slots* that need to be filled w/ commands that make up input to the state machine 
	- slots indexed by *slot number* 
- replicas receive requests from clients and assign them to specific slots, creating a sequence of commands
- replica, on receipt of a `(request, c)` message, proposes command, `c`, for its lowest unused slot.
- hence, the tuple `(slot, command)` constitutes a *proposal* for slot *s*
- in concurrently operating clients, different replicas can propose different commands for the same slot 
	- avoided using *consensus protocols* - runs between the *configuration* of the slot
	- the configuration consists of the leader and the acceptors. (**note, no replicas!**)
- paxos can reconfigure - client just proposes a special reconfiguration command 
	- this is also decided in a slot *s*
	- however, this reconfiguration does not take effect until `s + WINDOW` 
	- allows up to `WINDOW` slots to have proposals pending 

## States and invariants

### Replica variables
1. *state*: replica's copy of application state 
2. *slot.in*: index of next slot which the replica has not yet proposed any command (next empty slot) 
3. *slot.out*: next slot that it needs to learn a decision before it can update its copy of app state. 
	1. this is equivalent to state's version number 
4. *requests*: set of requests that replica has received and *not yet proposed or decided*
5. *proposals*: outstanding proposals 
6. *decisions*: set of **decided** proposals (implies that the slot is also filled, as a proposal is a tuple of `(slot, command)`) 
7. *leaders*: set of leaders in corrent config; initial leaders are passed as argument 

### Invariants

1. There are no two different commands decided for the same slot
2. All commands up to *slot.out* are in the set of decisions
3. For all replicas *p*, *p.state* is the result of applying the commands in the set of decisions to the initial state for all slots up to *slot.out* in order of slot number. 