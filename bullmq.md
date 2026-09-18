# groups
- each group in bullmq is dictated by its `groupId` 
- the jobs are taken in round robin fashion and if we are not yet at the batch limit but have exisitng jobs that belong to the `groupId`, then we can take the job as part of the batch