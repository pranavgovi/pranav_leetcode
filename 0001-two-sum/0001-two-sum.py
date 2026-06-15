class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        nums = list(zip(range(n), nums))
        nums.sort(key= lambda x:x[1])
        print(nums)
        left, right = 0, len(nums)-1
        while left<right:
            tot = nums[left][1]+ nums[right][1] 
            if tot == target:
                return [nums[left][0],  nums[right][0]]
            elif tot>target:
                right-=1
            else:
                left+=1
