# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        """
        one node- create a node for it and return it
        """
        if len(preorder)==1:
            return TreeNode(preorder[0])
        
        def recursive(preorder, inorder):
            if not preorder:
                return
            
            root=preorder[0]
            root_index = inorder.index(root)
            root_node = TreeNode(root)
            root_node.left = recursive(preorder[1:root_index+1], inorder[:root_index])
            root_node.right = recursive(preorder[root_index+1:], inorder[root_index+1:])
            return root_node
        
        return recursive(preorder, inorder)