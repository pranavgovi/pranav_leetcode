class Solution:
    def isGood(self, nums: List[int]) -> bool:
        n=len(nums)
        #so n-1 should occur 2 two times all other number 1 time
        lookup={}
        for num in nums:
            if num not in lookup:
                lookup[num]=0
            lookup[num]+=1

        
        for i in range(1,n):
            if i not in lookup:
                return False
            elif i!=n-1 and lookup[i]>1:
                return False
            elif i==n-1 and lookup[i]!=2:
                return False
        if len(nums)<2:
            return False

        return True