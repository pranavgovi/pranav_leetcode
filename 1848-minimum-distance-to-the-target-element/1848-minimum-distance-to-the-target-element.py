class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mini = float('inf')
        for ind, num in enumerate(nums):
            if num==target:
                mini=min(mini, abs(ind-start))
        return mini