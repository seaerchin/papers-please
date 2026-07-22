# postgres advisory locks
- Postgres does not enforce the use of these locks - up to the application to use them correctly 
	- common use case: emulate pessimistic locking strategies - advisory locks are faster, avoid table bloat and automatically cleaned up at end of session
- 2 ways to acquire an advisory lock: session or tx level

## Session level locks

> [!NOTE] Session level lock duration
> A session level advisory is held until explicitly released or the session ends - session level locks DO NOT honor tx semantics

- Session level locks **DO NOT** honour transaction semantics: a lock that is held during a tx will still be held **even if the tx is rolled back**
- similarly, an unlock is effective even if the calling tx fails 
- a lock can be acquired multiple times by its owning process - but in order to release, we need to also release the lock.
	- for example, i acquire lock x 2 times - i need to also release it 2x in order for the lock to be available to other callers to acquire
## Transaction level locks
- These behave similarly to regular lock requests
	- auto released at the end of the tx 
	- no explicit unlock operation
	- more suited to short term usage of a advisory lock 

## Interactions

> [!NOTE] Lock semantics 
> - If a session holds an advisory lock, additional requests to lock **will always succeed** even if other sessions are awaiting the lock 
> - **THIS IS TRUE REGARDLESS OF LOCK TYPE** (session/transaction level)

- A session level lock will block acquire of a tx lock for the same advisory lock and vice versa 
## misc
 - can query via `pg_locks` system view
 - both advisory + regular locks are stored in a shared memory pool
	 - the size of the pool is defined by `max_locks_per_transaction` + `max_connections`
	 - once this pool is exhausted, the server will not grant any locks