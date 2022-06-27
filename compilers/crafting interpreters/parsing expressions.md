# ambiguity 
- ambiguity can exist in our parser if we don't settle *precedece* and *associativity*.
	- take for example (6 - 2 * 3 / 3) -> if we don't define precedence, this can be written as (6 - 2) * 3 / 3. 
	- similary, if we don't define associativity, we can treat this as 6 - 2 * (3 / 3), whicih is not what we want. 
	- all of these differ from the correct result of 6 - ((2 * 3) / 3)

## associativity 
- operators can be left/right associative. this affects the logical grouping order (from left/right) 

# left recursion 
- left recursion for a production rule (something -> something | some other thing) is difficult to handle in a LALR parser because it will infinitely recurse 

# strategies 
1. lox stratifies the grammar into different precedence lvels, where the rule matches expressions at its own level or higher. 

>expression     → literal
               | unary
               | binary
               | grouping ;
literal        → NUMBER | STRING | "true" | "false" | "nil" ;
grouping       → "(" expression ")" ;
unary          → ( "-" | "!" ) expression ;
binary         → expression operator expression ;
operator       → "==" | "!=" | "<" | "<=" | ">" | ">="
               | "+"  | "-"  | "*" | "/" ;

# recursive descent parsing
- we need to ensure no left recursion as it might lead into an infinite loop 
	- eg: a -> a | "something" will cause the parser to keep leading into a
	- we can just rearrange 
- we need to have precedence (see [[#ambiguity]]). as we are using recursive descent , we could split up our rules by precedence and write our parser from the top-down (highest priority should be tried last)
	- this means that we always try the lower priority first and then if it fails, try to match something of a higher priority