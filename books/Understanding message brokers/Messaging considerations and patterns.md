# Summary 

## failures 
### sending failures
- take note: this is on sending a message to my broker
- need to be aware of sending model of the broker - sync sends can block my app thread forever on failure 
- async sends can cause mem leaks if the buffer isn't consumed 
- can consider using a circuit breaker pattern where we transit from ok -> error when sending fails
	- then we transit error -> retry and if send succeeds then retry -> ok else retry -> error 
### consuming failures 
- 2 types - permanent and temp
	- interesting case of permanent failure: **messages that are not forward compat**
	- in this case, your consume will always fail to process 
	- abit vague - if i can consume but cannot process, the message is already freed form the broker, no? unless the implication is that because i am unable to process, my app dies

#### permanent failures 
- Q: why fall back to broker redelivery? 
- once failure count exceeds some amount, shift message into dlq 
	- how does this help? can keep retrying bad messages so easier debug is my assumption

#### temp failures 
- can be global (affecting all) or local (only cur message)
- sane strat for local is to just retry - local implies failure is transient as it's most probably related back to message directly so retry is sane strat
- i'd need some way of distinguishing in practice, because i only know failures are global past some n amount of local failures right? 

(these are availability failures - correctness failures leh?)

### idempotency 
- need some durable storage + unique key -> we always write in 
- lazy risk of dup
- eager risk of no process