class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        l,r =0 ,0
        
        #initially range is l,r =0
        cnt=0
        while r<n-1:
            cnt+=1
            maxi =nums[l]+l
            ind=l
            for i in range(l+1, r+1):
                if i<n and nums[i]+i > maxi:
                    maxi = nums[i]+i
                    ind = i
            l= r+1
            r = maxi
          
        return cnt
    