# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        """
        1. root to leaf paths equal to sum
        2. there can be negative values
        handle:
            if root none
            duplicate paths?

                5 curr_sum=0, []
            recur(4, sum=5, [5])           recur(8, sum=5, [5])
            recur(node11, sum=9, [5,4])
        recur(node7, sum=20, [5,4,11])    recur(node=2, sum=20, [5,4,11]) = 5,4,11,2 valid append 
        i have to pop 2 back since lists are  mutable
        """
        if not root:
            return []
        answer = []
        def recursive(node, path_sum:int, path: List[int]):
  
            path.append(node.val)
            path_sum+=node.val
            if path_sum == targetSum and not node.left and not node.right:
                answer.append(path.copy())
            
            if node.left:
                recursive(node.left, path_sum, path)
            if node.right:
                recursive(node.right, path_sum, path)
            #remove the appended node
            path.pop()
            return
        recursive(root, 0, [])
        return answer

        """
                                    func(Node =5,sum =0, [])
        func(Node4, 5, [5])                                     func(NBode=8, sum=5, [5])
                                                            func(node13, 13, [5,8])  func(node4,sum=13, [5,8]) =17, [5,8,4]
                                                            5,8,4,5 
                                                                     =26 path 5,8, 13 
                                                                     pop 13 back            




    func (Node11, 9, [5,4]) 11 wwill get appended functions are clalled , rmeove 11
    func (node7,20 , [5,4,11] ) fuinc(node2, 20, [5,4,11] )
    => 27 nto valid                 [5,4,11,2] 22 accepted
        """

