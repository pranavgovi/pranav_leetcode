class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write= 0 
        n=len(nums)
        for i in range(n):
            if write<2 or nums[write-2]!=nums[i]:
                nums[write] = nums[i]
                write+=1
        return write