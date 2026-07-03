- events can have [metadata](https://www.intercom.com/help/en/articles/175-set-up-event-tracking-in-intercom) tied to them
- the key names (presumably event names) are case insensitive + has restrictions on special characters (safest to just use alphanum)
	- dashes in key names are also not displayed in intercom
# Intercom JS API
- use `Intercom('trackEvent')` api like so: `Intercom('trackEvent', ‘upload-complete')` ; can also include an optional `metadata` argument - `Intercom('trackEvent', ‘upload-complete', metadata)`
- in order to track using the JS API, intercom needs to load first - probably not a big deal for Studio

--- 

# Best practices 
1. **Send events which capture meaningful actions**. A purchase is a great basis for a conversation as opposed to recording all the clicks that lead up to that purchase. Meaningful events will also make creating filters and auto-messages much easier.    
2. **Send the right amount of metadata**. Metadata is a great way to contextualise activity, but sending too much can be distracting. Remember that you can always link back to your own systems for more details.
3. **Format your metadata as if it were to be sent to a customer.** Metadata is not formatted when included in your messages, so it must be ready to go when it’s received by Intercom.
4. **Use events to understand user to user interactions** like invitations and social activity. You can use metadata to provide a rich view of how users are interacting with your business and each other.
5. **Name your events in a way that makes them easily readable** in Intercom. Using a past tense verb is one way to make the action more easily understood when it appears in the user activity timeline e.g. "**Purchased** item", "**Created** profile" or "**Viewed** onboarding guide".


--- 
# event based messaging
- use event rule 
- can also adjust frequency of messaging based around certain rules 