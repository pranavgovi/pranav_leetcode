class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        """
        WHENEVER WE are inputting an element remove all smaller values also everytime remove out of window elements'
        1 3 4 5 6 k=3
        i-k >= 

        """
        ans=[]
        from collections import deque
        queue= deque() #double ended queue thta can pop/push front pop/push back
        #queue will have (ind, value)
        for i, num in enumerate(nums):

            while queue and i-k >= queue[0][0]:
                queue.popleft()

            while queue and queue[-1][1]<=num:
                queue.pop()
            queue.append((i,num))

            if i>=k-1:
                ans.append(queue[0][1])
        return ans
