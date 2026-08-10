class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #this problem can be divided into subproblem leading to the main ans
        #because for every (i,j) it depends on what we include / exclude in the sequence
        #if i>=m or j>=n return 0
        #if both chr match we just return 1 +  max(skip left,  right stays), (left stays,move right , move both)

        # memo={}
        m,n=len(text1), len(text2)

        # def dp(i,j):
        #     if (i,j) in memo:
        #         return memo[(i,j)]
        #     if i>=m or j>=n:
        #         memo[(i,j)]=0
        #         return 0
        #     if text1[i]==text2[j]:
        #         memo[(i,j)]=  1 + dp(i+1, j+1)
        #         return memo[(i,j)]
        #     memo[(i,j)]= max(dp(i, j+1), dp(i+1, j), dp(i+1, j+1))
        #     return memo[(i,j)]
        # return dp(0,0)
        #base condition is when char match return 1 + dp[i+1][j+1]
    
        dp= [[0]*(n+1) for _ in range(m+1)]
        for i in range(m-1,-1,-1):
            for j in range(n-1,-1,-1):
                if text1[i]==text2[j]:
                    dp[i][j]= 1+ dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j], dp[i+1][j+1])
        return dp[0][0]