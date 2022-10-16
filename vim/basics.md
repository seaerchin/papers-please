# operators
a: append
d: delete 
p: put 
x: delete char
c: change
g: goto
	- we can use  `shift-g`  to easily go to a specific line
s: substitute
	- we can extend this functionality wtih regex!!: 
	- `:s/<regex>/<new_text>`
v: visual mode
	- shift-v is **line mode**


# motions
some examples of motions
- w: (start of) word 
- e: end (of word) 
- $: eol
- 0: start of line

# operators 

- vim operates on operators and motions
	- an example is d$ -> the operator is d (delete) and the motion is $
	- we can repeat the (operator, motion) tuple by prefixing w/ number
		- eg: 3dw deletes 3 words 

## commands 
- use / to find a pattern 
	- use n to go forward,  shift-n to go backwards 
- ? to find a pattern *starting from the back* (ie, from cursor to start of file)
- % to match parens 