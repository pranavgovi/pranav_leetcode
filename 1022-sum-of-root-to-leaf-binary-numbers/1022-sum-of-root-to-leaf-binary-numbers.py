# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def binaryTonum(st):
            print(st)
            x=len(st)

            value=0
            
            for i in range(x-1,-1,-1):
                value+= (int(st[i])* (2**(x-1-i)))
            return value
        ans= 0
        def traverse(node, path):
            nonlocal ans
            if not node:
                return
            path.append(str(node.val))
            if not node.left and not node.right:
                #it is a leaft
                ans+=binaryTonum(''.join(path))
                path.pop()
                return
            traverse(node.left, path)
            traverse(node.right, path)
            path.pop()
            
        traverse(root,[])
        return ans
