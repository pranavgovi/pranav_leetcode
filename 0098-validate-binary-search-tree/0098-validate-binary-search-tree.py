# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def traverse(node, min_limit, max_limit):
            if not node:
                return True
            return min_limit<node.val<max_limit and traverse(node.left, min_limit, node.val) and traverse(node.right, node.val, max_limit)
        return traverse(root, float('-inf'), float('inf'))
            
            
