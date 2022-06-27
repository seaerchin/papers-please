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
