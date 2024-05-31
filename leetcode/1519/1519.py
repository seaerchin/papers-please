import typing
from collections import defaultdict

def from_edges(edges): 
    tree = defaultdict(list)
    for edge in edges:
        f = edge[0]
        t = edge[1]
        tree[f].append(t) 
    return tree

def combine(sub, d): 
    for i in sub.items(): 
        k, v = i
        d[k] += v
    return d

def iter_tree(node, tree, labels):
    d = defaultdict(lambda: 0) 
    if len(tree[node]) == 0: 
        d[labels[node]] += 1 
        ret = [0 for _ in range(len(labels))]
        ret[node] = d[labels[node]]
        return {"d":d , "ans": ret} 
    
    for nnode in tree[node]: 
        ret = iter_tree(nnode, tree, labels)
        d = combine(ret["d"], d)
        ret["ans"][node] = d[labels[node]]
    print("d", d, tree)
    return {"d":d , "ans": ret["ans"]} 

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        tree = from_edges(edges)
        return iter_tree(0, tree, labels)["ans"]
