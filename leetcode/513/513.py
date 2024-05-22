# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import typing
from collections import deque, defaultdict

def bfs(root):
    res = defaultdict(lambda: []) 
    res[0].append(root)
    if not root: 
        return res 

    q = deque([root])
    level = 1 

    while q: 
        l = len(q)
        for _ in range(l):
            cur = q.popleft() 
            if cur.left: 
                q.append(cur.left)
                res[level].append(cur.left)
            if cur.right: 
                q.append(cur.right)
                res[level].append(cur.right)
        level += 1 

    return res

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        levels = bfs(root)
        max_l = max(levels.keys())
        return levels[max_l][0].val

