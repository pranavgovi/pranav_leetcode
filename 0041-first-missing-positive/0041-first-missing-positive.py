class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        for i in range(n):
            if nums[i]>n or nums[i]<=0:
                nums[i]=0
        NEG=-(n+1)
            
        for i in range(n):
            val =abs(nums[i])
            if 0<val<=n : #valid number
                #mark i-1 as a negative number
                if nums[val-1]>0:
                    nums[val-1]*=-1
                elif nums[val-1]==0:
                    nums[val-1]=NEG

        
        for i in range(n):
            if nums[i]>=0:
                return i+1
        return n+1