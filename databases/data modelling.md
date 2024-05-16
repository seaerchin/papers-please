---
id: data modelling
aliases: []
tags:
  - trees
  - databases
  - database
---

# Storing trees in db 
4 common techniques 

## Materialised paths

## Parent pointer 
- set parent pointer on the row -> every row will now point to its parent, if available
- nested reads are not good unless we use recursive CTE, so that we will query the entire table at 1 go
- means that we have to do single level reads at a time (maybe this is ok?)

### Create 
- create node (row in db), set parent 

### Read 
- single reads ok, esp if we have id given
- nested reads abit more complex, need recursive queries 

### Update 
- if leaf node, update is trivial. 
- if update node w/ child, still ok -> child node will point back by parent 
- IMPORTANT: the parent doesn't actually know about their child -> only child knows their parent 
  - to get the child of a node, we have to run a query

### Delete
- if i delete a node w children, the child might not know? (since no FK out to another table, we cannot cascade delete)

## Nested sets 

## Closure tables
- store graph separately from data 
- graph is stored in a separate table 

| node_id | parent_id | depth |
| ------------- | -------------- | -------------- |
| 2 | 3 | 4 |


