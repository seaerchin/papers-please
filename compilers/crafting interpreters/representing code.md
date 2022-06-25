# rules for grammars 

- we can't possibly produce an exhaustive set for the possible strings of our grammar as it is infinite
	- instead, we go from another direction - we specify a *finite grammar* that we use to create the strings 
    - strings created in this fashion are called *derivations* whereas the rules are called **productions** (for their respective roles)

- productions can be categorized into 2 categories
	- *terminal* - a letter from the grammar's alphabet 
	- *non-terminal*  - a **named reference** to another rule in the grammar 

# visitor pattern
- the *expression problem* is at the core of why the visitor pattern exists. in essence, oop vs fp views data/functionality along 2 axis.
	- object oriented languages make adding new data types easy (we can simply `extend`), but adding new functionality across to those data types is hard -> we have to add that functionality across to every single class that exists  
	- fp makes adding new functionality easy (just add a new function and pattern match) but adding new data types is hard as we have to add a new case to every single `match` statement 

- the visitor pattern solves this by adding a new visitor class that accepts a union type that can represent all the types. 
	- this visitor class then has a single method (typically `visi6t`) that calls the accept argument of each class with the instance itself. 
	- this is essentially doing double dispatch (first to the visitor then to the base class)
	- now, when we want to add new functionality, we simply have to add it in the visitor class rather than every single associated class 
	- 