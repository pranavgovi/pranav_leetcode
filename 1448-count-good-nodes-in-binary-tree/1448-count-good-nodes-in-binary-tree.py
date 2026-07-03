# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        ans=0

        def traverse(node, max_seen):
            nonlocal ans
            if not node:
                return 
            if node.val>= max_seen:
                ans+=1
            traverse(node.left, max(max_seen, node.val))
            traverse(node.right, max(max_seen, node.val))
            return
        traverse(root, float('-inf'))
        return ans            

