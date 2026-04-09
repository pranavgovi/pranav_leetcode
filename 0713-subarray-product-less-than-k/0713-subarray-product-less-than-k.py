class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        curr_prod = 1
        left=0
        right=0
        answer=0
        n=len(nums)
        while left<=right and right<n:

            curr_prod *= nums[right]
            while left<=right and curr_prod>=k:
                #we can move left
                    curr_prod = curr_prod // nums[left]
                    left+=1
           
            answer+= (right-left+1)
        
            right+=1
        return answer