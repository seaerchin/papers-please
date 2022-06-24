# Interpreter Framework 
- lox reads directly from the source file as it is a *scripting language* 
	- 2 ways of execution -> either from source file or through IDLE
- principle of **maximal munch** - we always try to consume the longest input string possible
- note that we can use a parser combinator (i think) to write the parse function from string into tokens but will stick to the one given here for close adherence to the source material           