alot of operators in rust is implemented under the hood via traits; for example: 
- `==` uses `PartialEq` under the hood
- `for .. in` also uses the `Range` trait 