class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        answer=0
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited= [ [0]*n for _ in range(m)]

        def dfs(r,c):
            nonlocal count
            count+=1
            visited[r][c]=1
            for dir in directions:
                a,b=dir
                new_r, new_c = a+r, b+c
                if 0<=new_r<m and 0<=new_c<n and not visited[new_r][new_c] and grid[new_r][new_c]==1:
                    dfs(new_r, new_c)
        
        for i in range(m):
            for j in range(n):
                count=0
                if grid[i][j]==1 and not visited[i][j]:
                    dfs(i,j)
                    answer= max(answer, count)
        return answer