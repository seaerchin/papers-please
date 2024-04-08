- can't seem to get db populated with data
	- tried `seed:run` after `seed:gen`
	- also tried `local-setup` 
- frontend just shows me loading spinner
	- set `referralId` to 1 but we require `uuid` 
	- `usePublicReferral` has a sane default though? 
- lack of knowledge on NestJs so need to brush up
	- roughly self-explanatory though
	- going by endpoint

# `/api/v1` 


> [!NOTE] Knowing when is good enough
> good pattern of less is more -> rather than locking in the wrong abstraction, 
> just make a "good-enough" solution until we have time to do it later

## `api-holding.controller.ts`
