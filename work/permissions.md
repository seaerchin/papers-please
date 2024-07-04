---
id: permissions
aliases: []
tags:
  - rbac
  - abac
---

# RBAC 
- user -> role -> permissions
- a user's permissions is defined solely by their role

# ABAC 
- (A1, A2, A3) -> permissions

# Comparison
Given n boolean value attributes, in order to achieve granular controls across all n attributes, 
- ABAC requires 2^n rules for evaluation
- RBAC requires 2^n roles for evaluation

- ABAC makes the trade-off upfront (all the rules need to be comprehensively defined, otherwise i will run into edge cases)
- RBAC makes the trade-off later (i can segment into buckets -> assign roles based on buckets) but means that initial permissions model wouldn't be as fine grained 

/> [!NOTE] ReBac 
> it feels like ReBAC can be formulated in terms of ABAC? 

- paper argues for (U -> R -> A, A1, A2, ... An) -> Perms
  - hard work is to identify the set of dynamic/static attributes
  - dynamic -> A1, A2 ... An 
  - static: U -> R -> A

# Relevance to isomer
- we only have to answer crud + publish 
- set of resources: folders/pages/users

initially, 
- Roles = [publisher, editor, admin]
- no attributes 
- how do i answer a query if an editor has permissions to edit any page?
  - i still need to do a db lookup
  - still need to check if page -> folder
  - possible to work around if i define attributes as being the set of top level folders

# accesscontrol (lib)
- defines attributes as being properties on resources
- evaluating essentially means "what actions am i allowed to take on the properties of this resource"

