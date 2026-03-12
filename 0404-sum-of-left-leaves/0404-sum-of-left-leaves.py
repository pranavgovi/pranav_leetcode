# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        answer=0
        def traverse(node):
            nonlocal answer
            if not node:
                return 0
            if node.left and not node.left.left and not node.left.right:
                answer+= node.left.val
                #the above node is a left leaf 
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return answer