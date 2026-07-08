# heartbeat vs expiration
- heartbeat works by having a worker issue a ping to a given heartbeat URL. this signals that the worker **is still alive and working on the job**
- expiration works by killing a job when it exceeds the **maximum allowed time for it**; past this time, the job is assumed to be stale and no longer relevant

|                      | Heartbeat                                                                  | Expiration                                                                                     |
| -------------------- | -------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| **Purpose**          | Detect dead workers quickly                                                | Abandon stale job attempts                                                                     |
| **What it means**    | The worker stopped responding — the job is still valid, retry it elsewhere | The job has been active too long — this attempt is no longer relevant                          |
| **Failure scenario** | Worker crash, OOM kill, network partition, node shutdown                   | Infinite loop, deadlock, unresponsive external dependency, or simply exceeding the time budget |
| **Detection speed**  | Fast (seconds to minutes)                                                  | Matches expected job duration                                                                  |
| **Default**          | Disabled                                                                   | 15 minutes                                                                                     |

# when to use which
- use `heartbeat` to lower MTTR for workers - since it acts as a liveness check for worker, the most time we will ever go before knowing that a worker is down is the time between each heartbeat
- use `expireInSeconds` when we want to kill long running job 