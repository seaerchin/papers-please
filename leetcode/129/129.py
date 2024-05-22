# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def is_leaf(root): 
    if not root: return False 
    return not root.left and not root.right

def dfs(root, cur) -> int: 
    if is_leaf(root): return cur * 10 + root.val
    left_sum = dfs(root.left, cur * 10 + root.val) if root.left else 0
    right_sum = dfs(root.right, cur * 10 + root.val) if root.right else 0
    return left_sum + right_sum

class Solution:
    def sumNumbers(self, root) -> int:
        if not root: 
            return 0 
        return dfs(root, 0) 


