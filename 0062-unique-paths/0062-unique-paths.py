class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        at any cell, number of ways is dp[i+1][j] + dp[i][j+1]
        base condition m-1th row has 1 way, 
        n-1th col has 1 way
        recurrence = dp[i+1][j] + dp[i][j+1]
        while trvaersing last row and col should not go out of bounds
        so initialise the dp with m+1 and n+1 col
        """
        dp= [ [0]*(n+1) for _ in range(m+1)]
        #1 path to reach m-1,n-1 from m-1,n-1

        for i in range(m-1, -1,-1):
            for j in range(n-1, -1,-1):
                if i==m-1 and j==n-1:
                    dp[i][j]=1
                else:
                    dp[i][j] = dp[i+1][j] + dp[i][j+1]
        return dp[0][0]

