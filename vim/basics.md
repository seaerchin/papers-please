# operators
a: append
d: delete 

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