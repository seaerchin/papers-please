# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import defaultdict, deque

def child_vals(root): 
    left_val = root.left.val if root.left else 0 
    right_val = root.right.val if root.right else 0 
    return left_val + right_val

def dfs(root, levels, child_vals, depth = 0): 
    cur_val = levels[depth] - child_vals 
    root.val = cur_val 
    dfs(root.right, depth + 1, levels, child_vals(root)) 
    dfs(root.left, depth + 1, levels, child_vals(root)) 

class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        levels = defaultdict(lambda: 0)
        cur_level = 0
        if not root: 
            return None 
        
        q = deque([root]) 
        while len(q) > 0: 
            l = len(q)
            s = 0 
            
            nodes = deque([])
            for _ in range(l):
                cur = q.popleft()
                nodes.append(cur)
                s += cur.val 
                if cur.left:
                    cur.left.parent = cur
                    q.append(cur.left)
                if cur.right:
                    cur.right.parent = cur
                    q.append(cur.right)
            levels[cur_level] = s
            s = 0 
            cur_level += 1 

        dfs(root, levels, root.val, 0)
        return root
        

