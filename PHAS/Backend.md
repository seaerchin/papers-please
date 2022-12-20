- enroll user into HSG via `POST`
	- `POST api/v1/public/hsg/enroll`
	- need to write through to the database

```json
{ 
  patient: UserInputWithDob, 
  institutionId: integer, 
  hsg_token: string
}
```

- FE -> BE relevant values of user (see ^)
- sanitise the data
	- need define DTO and validate
- write through to the database
- fire off sms
	- based on the type of the hsg institution that the user selected, fire off different variants of SMS