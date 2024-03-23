# stack alloc

- most allocations go to stack by default
```rust
fn foo() {
    let y = 5;
    let z = 100;
}

fn main() {
    let x = 42;

    foo();
}
```

- in this example, we allocate 
```
(Addr: name, value)
2: z, 100
1: y, 5
(enters foo here)
0: x, 42 
```

# heap alloc 

```rust 
fn foo(i: &i32) {
    let z = 42;
}

fn main() {
    let x = 5;
    let y = &x;

    foo(y);
}
```

- in this example, we allocate: 
```
(Addr: name, value)
3: z, 42
2: i, -> 0
(enters foo here)
1: y, -> 0 (pointer to 0)
0: x, 5 
```

- note here that `y` and `i` both point to the same variable, `x`. as they are both pointers, `i` **copies** the underlying pointer to the value instead of pointing to `y`.
- 