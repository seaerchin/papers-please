# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def walk(target, root):
    if not root: 
        return [] 
    cur_cost = root.val 
    cur_path = []
    if cur_cost > target:
        return [] 
    left_paths = walk(root.left)
    right_paths = walk(root.right)
    # need to map to each path returned
    if left_paths:
        cur_path.map(lambda x: x.append(left_paths))
    if right_paths: 
        cur_path.map(lambda x: x.append(left_paths))
    return cur_path

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = walk(targetSum, root)
        return paths 


