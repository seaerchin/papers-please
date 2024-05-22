# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

import typing
from collections import defaultdict, deque

# returns the level sums 
def bfs(root):
    res = defaultdict(lambda: 0) 

    if not root: 
        return res 

    q = deque([root])
    level = 0 

    while q: 
        l = len(q)
        s = 0
        for _ in range(l):
            cur = q.popleft() 
            s += cur.val
            if cur.left: 
                q.append(cur.left)
            if cur.right: 
                q.append(cur.right)
        res[level] = s 
        level += 1 

    return res 

class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        level_sums = bfs(root)    
        vals = level_sums.values()
        if k > len(vals): 
            return -1
        return sorted(vals, reverse = True)[k-1]
