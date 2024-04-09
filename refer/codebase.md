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

note to self: read critically - ask why the code is structured the way it is and the underlying assumptions that it makes

codebase has no test - are we in growth phase? when is the right time to start? maybe first major launch ba 
## `api-holding.controller.ts`

`GET getReferralEligibility` 
- **QUESTION:** what's the difference b/w the type used in `@ApiQuery` and in the method itself? why not just use both?  
- **ANSWER**: `@ApiQuery` is swagger only -> follow-up: why cannot just use one and define `@ApiProperty`? saves trouble of manual sync 
- get offering, chas then return 
- **QUESTION:** why boolean for `referral + subsidy`? seems difficult to extend but maybe interest of time?
- `getChas` 
	- first thought -> parse, don't validate but maybe a knee jerk reaction ba
	- stupid question - `year` is tz dependent???
	- (don't get `wretch`, seems to be `axios` but better)
	- **QUESTION:** what's the abstraction boundary between `service/controller`? prior codebases draw the line at router does validation etc and service is function w/o external io -> benefits is imperative shell, functional core -> easier to test/reason/validate (maybe too heavy to do anyw)

`GET listReferrals` 
- `paginatedRes` is pretty lit 
- just list referrals then transform
- **QUESTION:** why paginate here? seems to be optimising for small packet size based off prior convos. not sure if we should be paginating or whether got other solutions 
- `referralService.listReferrals`
	- not entirely sure i agree w/ mutation on query builder but i don't really have a better way too -> dev understanding is clear i g?
	- (we hard code pagination params here whereas in other systems we present a pagination token; see [here](https://cloud.ibm.com/docs/api-handbook?topic=api-handbook-pagination#token-based-pagination) for article that i never read lol)

`POST createReferral`
- `institutionService.createIfNotExists`
	- just use `upsert` ba
- `referral.service.createReferral`
	- scary as fk
	- (**QUESTION:** how does nest handle async errors? still via serialiser of thrown error?)
	- start state is `processing` 
	- in effect, this method is saying i need to have all of the given parameters **before** i can have a referral. not sure if we can relax some of these requirements? (eg: possible to infer some stuff???)
		- patient stuff -> what they want referral for (`patient/offeringId/senderHciCode` etc)
		- timeslot stuff (`timeslotStartAt`)
		- doctor stuff 
	- what can we get if we relax some of these requirements? we can possible have referral intent? doctor wants a referral, let patient confirm their slot
	- kinda really hate the boolean because it's not meaningful by itself and not really extensible sadge
- we `sendReferral` using an outbound job queue but we don't actually know if it's successful?
	- we send dto eagerly -> ok because status is `processing` 
	- if upstream dies, how do we know? on ur end we will still have the record in db withuot any sentinel 
	- maybe we want to bind `createReferral` to success of `sendReferral`? or some notif idk

`GET offerings`
- skipping, standard list

`GET offerings/:offeringId`
- skipping, standard get one

`GET offerings/:offeringId/:timeslots`
- i love `serviceService`
- a timeslot is given by calling the **underlying institution's api**
- some level of chicanery to make it seem like it's the same thing between APIs 
- **a timeslot here is really just a marker of 2 timestamps**
	- **QUESTION:** why not `from, length`? tbh both seem equivalent? maybe if you'd wanna stack timeslots? (ie, is computing from + length vs having to easier?)
	- **QUESTION:** this may be answered by reading the codebase but what exactly then determines a timeslot booking? ie, that this `[from, to]` has been assigned to a person?
		- this seems to be `offering`, which i thought was an actual medical checkup???
