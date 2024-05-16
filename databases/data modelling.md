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
- store the path down from parent to current node. 
- for eg, we have a path table in the db and this would read: `A -> B -> C`
- we will only use this to enforce the graph structure 

> [!NOTE] Referential Integrity 
> Database cannot preserve referential integrity here (ie, that all nodes in your path exist) 
> Our application has to take over this logic and sure that all moves use a write-lock 
> 
> Consider: if we have `A -> B -> C` and we shift to `A -> C -> B` whilst a rename `C rename to D` is underway
> Outcome: can be `A -> C -> B` (move wins) or `A -> B -> D` if rename wins

- sub-tree lookups in this case are relatively inexpensive + easy to do because we can just do regex match on the prefix of the path
- not too sure how efficient this is as it does use string matching (perhaps across the full table?) 

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

> [!NOTE] Summary 
> Easy to reason about and moves are relatively cheap 
> 
> However, queries wrt sub-trees are difficult to perform -> this is best suited for a read heavy pattern where the reads are done level by level and sub-tree reads are relatively rare.
> 
> Referential integrity because you can ask the db to enforce that parent_ids must exist in id

### extensions 
- we could use recursive common table exprs (supported in pq) to get descendants/ancestors in single query 
- could also point to different tables for the type of the node; this models inheritance (see [here](https://leonardqmarcq.com/posts/modeling-hierarchical-tree-data), under modelling subtype-specific attributes)

### consideration
- how is consistency involved here? specifically, path consistency -> we need to lock so that writes to the path of the same sub-tree don't wonk

## Nested sets 

## Closure tables
- store graph separately from data 
- graph is stored in a separate table 

**closure table storing structure of the graph** 

| node_id | parent_id | depth |
| ------- | --------- | ----- |
| 2       | 3         | 4     |
|         |           |       |

- if i were to insert a node into the data table, i would also need to update the closure table
  - no update = orphaned node -> wrong
  - need to add >=1 record (if leaf then 1) 
  - insertion of a new non-leaf node requires alot of ops -> eg: A -> C now change to A -> B -> C
    - need to add new record first then amend records for A + C in the closure table 
    - same case for moving

### Create
- leaf creates cheap, creates of non-leaf nodes is expensive + unwieldy (oof)

### Read 
- very cheap to do nested reads (reads w/ depth >1) or reads at any particular level

### Update 
- prohibitively expensive if it involves altering the structure + very difficult to get right

### Delete 
- leaf easy 
- deletion of non-leaf nodes bad 

> [!NOTE] Summary 
> This structure seems optimised towards a very read-heavy workload, where the most common query pattern involves fetching the nodes up to some depth 
> Not good if the structure of the graph is likely to change often 

# References 
1. [Baeldung](https://www.baeldung.com/cs/storing-tree-in-rdb) 
2. leonardqmarcq's [modeling hierarchical tree data in pg](https://leonardqmarcq.com/posts/modeling-hierarchical-tree-data)