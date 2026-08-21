class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        if len(s)<len(t):
            return 0
        
        memo={}

        m,n = len(s), len(t)

        def dp(s_ind, t_ind):
            if (s_ind, t_ind) in memo:
                return memo[(s_ind, t_ind)]
            if t_ind==n:
                memo[(s_ind, t_ind)]=1
                return 1
            
            #if s completes before t
            if s_ind==m:
                memo[(s_ind, t_ind)]=0
                return 0
            
            #check if both of them match
            tot=0
            if s[s_ind]==t[t_ind]:
                #we have 2 chocies to make
                #either take it
                tot = dp(s_ind+1, t_ind+1)
                #skip it
                tot +=dp(s_ind+1, t_ind)
            
            else:
                tot = dp(s_ind+1, t_ind)
            memo[(s_ind, t_ind)]=tot
            return tot
        
        return dp(0,0)

            
