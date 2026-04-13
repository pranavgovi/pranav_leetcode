class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        mini = float('inf')
        left= start-1
        right=start
        n=len(nums)
        while left>=0 and right<n:
            if nums[right]==target:
                return abs(right-start)
            elif nums[left]==target:
                return abs(left-start)
            else:
                left-=1
                right+=1
        