# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

def isLeaf(root): 
    if not root: return False
    if root.left or root.right: return False 
    return True

# returns a list<list<int>>
# when we hit the root node, 
# return a list of lists if 
# we have the value required 
# otherwise,
def walk(target, root):
    # terminate here as we already 
    # hit the leaf nodes of the tree
    if isLeaf(root):
        if target - root.val == 0: 
            return [[root.val]] 
        else: 
            return []
    
    left_paths = [] 
    right_paths = [] 

    if (root.left): 
        left_paths = walk(target - root.val,  root.left)
    if (root.right): 
        right_paths = walk(target - root.val, root.right)

    ans = []
    base = [[]] if left_paths == [[]] and right_paths == [[]] else left_paths + right_paths 

    for val in iter(base):
        cur_path = [root.val] + val 
        ans.append(cur_path)

    return ans 

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root: return []
        paths = walk(targetSum, root)
        return paths 


