# rules for grammars 

- we can't possibly produce an exhaustive set for the possible strings of our grammar as it is infinite
	- instead, we go from another direction - we specify a *finite grammar* that we use to create the strings 
    - strings created in this fashion are called *derivations* whereas the rules are called **productions** (for their respective roles)

- productions can be categorized into 2 categories
	- *terminal* - a letter from the grammar's alphabet 
	- *non-terminal*  - a **named reference** to another rule in the grammar 