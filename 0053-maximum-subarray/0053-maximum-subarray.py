class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        global_var= float('-inf')
        local_var=0

        for num in nums:
            local_var+=num
       
            global_var= max(global_var, local_var)
            if local_var<0:
                local_var=0
        return global_var