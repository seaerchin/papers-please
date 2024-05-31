---
id: polynomials
aliases: []
tags: []
---

# Uniqueness proof 
/> [!NOTE] Theorem 2.3
> The zero polynomial is the only polynomial over R of degree at most n which has more than n distinct roots

- let f and g be 2 different polynomials passing through the set of points (x_1, y_1) ... (x_(n+1), y_n+1)
- at each point (x_i,y_i), f(x_i), f-g == 0. 
- since this implies that they have n+1 roots (as f and g intersect at n+1 points), f-g must be the 0 polynomial 
- hence, f == g (since f-g == 0 for all i => f = g)
