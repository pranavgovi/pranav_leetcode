class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        local = 0
        globall = float('-inf')
        for num in nums:
            local+=num
            globall = max(local, globall)
            if local<0:
                local=0
        return globall