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