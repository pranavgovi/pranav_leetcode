# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        from collections import deque
        if not root:
            return []
        answer=[]
        queue = deque()
        queue.append(root)
        while queue:
            answer.append(queue[-1].val)
            x = len(queue)
            for i in range(x):
                node= queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        return answer
            

