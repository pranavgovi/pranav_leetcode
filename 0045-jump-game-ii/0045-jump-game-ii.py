class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        #goal is to reach the last index of nums
        left = 0
        right = 0
        jump_count = 0
        i=0
        l,r=0,0
        while r<n-1: #if it reaches we can break the loop

            #for the current range we have to find the farthest and set the range for the next iteration
            far=0

            for i in range(l,r+1):
                far= max(far, nums[i]+ i)
            
            l, r = r+1, far
            jump_count+=1
        return jump_count
        
