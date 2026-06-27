"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        """
        if not root -> None
             1 -null                          
            2 ->3-> null
        4-> 5->  6- 7-null 
        level order approach - o(n) time and space
        """
        from collections import deque
        if not root:
            return None
        queue = deque()
        queue.append(root)
        while queue:
            x = len(queue)
            prev_node=None
            for i in range(x):
                curr_node = queue.popleft()
                if prev_node:
                    prev_node.next= curr_node
                prev_node = curr_node
                if curr_node.left:
                    queue.append(curr_node.left)
                if curr_node.right:
                    queue.append(curr_node.right)

            prev_node.next= None
        return root
            
                

     