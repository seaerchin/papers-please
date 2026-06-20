ratatui renders via a widget -> in usual apps, *everything* is a widget which means that we can just defer downwards

the usual loop of the program flow is as follows: 
- render your UI
- listen on keyboard events
- handle keyboard events
this takes place via a `loop`