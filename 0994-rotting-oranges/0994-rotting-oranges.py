class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        check fresh oranges at start if o return 0
        """
        from collections import deque
        m,n = len(grid), len(grid[0])
        directions= [(1,0), (0,-1), (0,1), (-1,0)]
        visited = [ [0]*n for _ in range(m)]
        queue= deque()
        fresh_count= 0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    queue.append((i,j))
                    visited[i][j]=1
                elif grid[i][j]==1:
                    fresh_count+=1
        
        if not fresh_count:
            return 0
        
        timer = 0
        while queue and fresh_count:
            timer+=1
            x=len(queue)
            for i in range(x):
                r,c =queue.popleft()
                for dir in directions:
                    a,b = dir
                    new_r, new_c = a+r, b+c
                    if 0<=new_r<m and 0<=new_c<n and not visited[new_r][new_c] and grid[new_r][new_c]==1:
                        fresh_count-=1
                        visited[new_r][new_c]=1
                        queue.append((new_r, new_c))
        
         
        
        if not fresh_count:
            return timer
        return -1