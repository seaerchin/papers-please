## Lexemes and tokens 
- lexical analysis aims to scan raw text and parse them into tokens called *lexemes*
- store lexeme *type* 
	- avoids having to do raw string comparison
- principle of **maximal munch** - we always try to consume the longest input string possible
- Also needs to report errors to ensure a good user experience.

> [!SUMMARY]
> Lexical analysis aims to *transform* the source into tokens. 
> Tokens need to contain enough metadata to be useful for other functionality of the scanner, such as error handling

## Scanning feedback loop 
