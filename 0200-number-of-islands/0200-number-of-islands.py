class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m,n = len(grid), len(grid[0])
        visited = set()
        directions = [(1,0), (0,1), (-1,0), (0,-1)]

        def traverse(r,c):
            visited.add((r,c))
            for dir in directions:
                a,b = dir
                new_r, new_c = a+r, b+c
                if 0<=new_r<m and 0<=new_c<n and grid[new_r][new_c]=='1' and (new_r, new_c) not in visited:
                    traverse(new_r, new_c)
        count=0
        for i in range(m):
            for j in range(n):
                if (i,j) not in visited and grid[i][j]=='1':
                    traverse(i,j)
                    count+=1
        return count