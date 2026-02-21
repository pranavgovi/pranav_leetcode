class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m,n = len(s), len(t)
        
    
        # def backtrack(ind1, ind2):
        #     nonlocal ways

        #     if ind2==n:
        #         #i reached the end
        #         ways+=1
        #         return 
        #     if ind1>=m:
        #         return
        #     if s[ind1]==t[ind2]:
        #         #i can either include or skip
        #         backtrack(ind1+1, ind2)
        #         backtrack(ind1+1, ind2+1)
            
        #     else:
        #         backtrack(ind1+1, ind2)
        # backtrack(0,0)
        # return ways
        #lets memoize from ind1, ind2 how many ways are there to reach end
        memo={}
        def dp(ind1, ind2):
            if (ind1, ind2) in memo:
                return memo[(ind1, ind2)]
            if ind2==n:
                #it reached the end
                memo[(ind1, ind2)] =1
                return 1
                #1 way possible
            if ind1>=m:
                memo[(ind1, ind2)]=0
                return 0
            
            if s[ind1]==t[ind2]:
                memo[(ind1, ind2)] = dp(ind1+1, ind2+1) +dp(ind1+1, ind2)
                return memo[(ind1, ind2)]
            
            else:
                memo[(ind1, ind2)] = dp(ind1+1, ind2)
                return memo[(ind1, ind2)]
        return dp(0,0)

