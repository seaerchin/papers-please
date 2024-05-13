# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# returns a list<list<int>>
def walk(target, cur, root):
    if not root and target == cur: 
        return [[]] 
    if not root: 
        return []
   
    left_paths = walk(target - root.val, root.left)
    right_paths = walk(target - root.val, root.right)
    
    # need to map to each path returned
    if len(left_paths) > 0:
        cur_path.map(lambda x: x + [root.val])
    if len(right_paths) > 0:
        cur_path.map(lambda x: x + [root.val])
    return cur_path

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        paths = walk(targetSum, root)
        return paths 


