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
        #get the level order 
        """
        1   for i if there is i+1, i.next = i+1
        2 3
        4 5 6 7
        """
        temp = root
        if not root:
            return None
        queue =deque()
        queue.append(root)
        root.next= None
        while queue:
            level =[]
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:

                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                level.append(node)
            
            for i in range(1,len(level)):
                level[i-1].next = level[i]
        return temp

