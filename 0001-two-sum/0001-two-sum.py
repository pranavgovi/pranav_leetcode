class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        target-nums[i] in map, we can return prev_ind, curr_ind
        """
        lookup= {}
        for ind, num in enumerate(nums):
            if target-num not in lookup:
                #pair not found yet
                lookup[num]=ind
            
            else:
                return [lookup[target-num], ind]
        
        #O(n) time and space