class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        memo={}
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        m,n = len(matrix), len(matrix[0])
    
        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]
            #for any i,j
            max_len = 1 #by not moving , staying at (i,j)
        
            for d in directions:
                a,b = d
                new_r, new_c= a+i, b+j
                if 0<=new_r<m and 0<=new_c<n and matrix[new_r][new_c]>matrix[i][j]:
                    max_len = max(max_len, 1+ dp(new_r, new_c))
            
            memo[(i,j)]=max_len
            return max_len
        maxi=1
        for i in range(m):
            for j in range(n):
                maxi = max(maxi, dp(i,j))
        return maxi
                