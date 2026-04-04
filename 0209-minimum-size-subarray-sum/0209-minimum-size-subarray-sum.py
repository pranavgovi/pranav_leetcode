class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        """
        keep expanding the window till the curr_sum<target.
        once when i reach curr_sum>=target shrink the window
        """
        left, right= 0 ,0
        curr_sum = 0
        n=len(nums)
        min_length = float('inf')
        while left<=right and right<n:
            curr_sum = curr_sum + nums[right]

            while left<=right and curr_sum>=target:
                #this is a valid window
                #move left
                min_length = min(min_length, right-left+1)
                curr_sum = curr_sum - nums[left]
                left+=1
            
            right+=1
        if min_length == float('inf'):
            return 0
        return min_length


