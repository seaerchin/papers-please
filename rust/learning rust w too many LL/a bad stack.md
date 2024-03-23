# unbounded representations

```rust
pub enum List {
	Empty,
	Elem(i32, List),
}
```

- this has unbounded size.
  - Data inside `struct`s and `enum`s (and tuples) is stored directly inline inside the memory of the struct value. Given a struct like the list above, the size of it is given by:
  - `sizeof List === sizeof i32 + sizeOf List`
  - which is recursive in nature to overcome this, we need a *pointer* to the sublist.

# bound representation with stack alloc

```rust
pub enum List {
	Empty,
	Elem(i32, Box<List>),
}
```

- let `[]` be stack alloc and `()` be heap. 
- when we use `List`, the first element will be heap allocated. if we had a list of 3 elements, it'd be: `[i32, ptr -> next], (i32, ptr -> next), (Empty, junk)`
## downsides
- in our code above, there will be a first element that is always stack allocated (as we don't hold a pointer to the start)
- during merging/splitting, this leads to a case where we have to shift from heap alloc -> stack alloc:
```
List 1: [A] -> (B) -> (C) 
to 
List 1: [A]
List 2: [B] -> (C)
```

involves alloc of `B` from heap onto stack 