
> [!NOTE] Goals
>  read critically - ask why the code is structured the way it is and the underlying assumptions that it makes
>  what can i offer in terms of this codebase **beyond** feature delivery 

**QUESTION:** what differentiates a file in `/worker` from elsewhere? terminology-wise, i'd assume that a file here would run apart from the main app + is async (my mental model is a cf worker/background process)
	**ANSWER:** files in `worker` only have a single call-site in `cron-jobs` - they are meant to be executed async (but will still eat main CPU monkas)

`syncPbOfferings`
- we gate `Promise.all` by `logger.info` 
	- suspect this is to get a strict time-bound? 
	- wonder if it'd be more useful to `trace` this explicitly instead if getting perf insight/observability is the main goal here
	- **NOTE:** since the behaviour of `Promise.all` is to fail when any one promise fails, it could be that we sync the offerings but **not the others**
		- we *might* end up with a view where offerings are updated but institutions are not (how likely is this even tbh)
- my assumption here (since they are all pointing to pb) that the source of truth is the pb api?
- `syncPbInstitutions`
	- uses underlying pb api to list the institutions 
	- `listPbInstitutions`
		- **QUESTION:** why is `allPbInstitutions` returned from a paginated api? (assumption: `maxResultCount` >> number of pb institutions)
			- follow-up: if this is indeed the case, why call it `getPaginatedInstitutions`? 
			- going to assume that the api is paginated but the page size (`maxResultCount`) we ask for is big enough to get all the institutions
		- **ANSWER:** API endpoint of `getPaginatedInstitutions` **is paginated**, we just want to exhaust all the items here. 
			- **QUESTION:** why make so many round trips over just asking once off? 
		- **QUESTION:** why `skipCount += maxResultCount` and not `skipCount += firstData.items.length`?
- after getting all pb institutions, from above method, just save
- (other 2 pb stuff is the same)
- `getAllPbOfferings` 
	- retrieve offerings from db 
	- maybe don't cast - type assertion seems safer
- filter where name !== sentinel then iterate over subspecialties to map them to an offering 
	- we default `name` to `institutionId` if it isn't missing -> the relying party is HAS and it maps it just to a view right? ie, that we rely on the actual user (doctor) to tell that this is not an actual `institutionName` but rather `institutionId`?
	- update old/new offering
- repeat for offerings
- **QUESTION:** why do we need to limit to 10? 
	- not too sure what's the mental model to adopt for `pLimit`
	- my assumption is that they queue the promises up till a limit (here 10)
	- **unlike** `promise.all`, i assume that each promise in the bundle of `limit` (10 here) **can fail independently**
	- it seems like we'd use this to limit max concurrency (maybe don't want to batter downstream?)
	- also that promises fail in isolation (**assumed**)
	
- **Summary**
	- if we assume a couple of things (downstream never fails, always returns most updated data) that makes this seem sync, this is a conceptually simple method where we:
	- fetch all data -> sync -> update new offerings -> map and return
	- **QUESTION:** how robust are our assumptions here

`updateOffering`
- eagerly `upsert newOffering`
- 