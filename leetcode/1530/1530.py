# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def get_child(nodes): 
    cur_level = []

    for node in nodes: 
        cur_level.append(node.left) 
        cur_level.append(node.right)

    return cur_level

class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        if not root: 
            return 0 
        nodes = [root]
        depth = 0

        while all(nodes): 
            cur_level = get_child(nodes) 
            nodes = cur_level
            depth += 1

        # need this because we want to construct a sliding window
        rem = distance % 2
        dist = distance - rem  

        window_size = dist // 2 + 1 
        num_iter = len(nodes) // window_size + 1 # if size < window_size, still need to iter once  

        for cur_iter in range(num_iter): 
            chunk = nodes[cur_iter:cur_iter + window_size]
            valid = filter(lambda x: x, chunk)
            
