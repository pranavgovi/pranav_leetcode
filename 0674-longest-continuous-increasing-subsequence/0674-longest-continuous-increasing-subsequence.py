class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        answer = 1
        n=len(nums)
        i=1
        start =0 
        while i<n:
            if nums[i]>nums[i-1]:
                answer =  max(answer, i-start+1)
                i+=1
                #valid
         
            else:
                #curr i is not a part
                start = i
                i+=1

        return answer