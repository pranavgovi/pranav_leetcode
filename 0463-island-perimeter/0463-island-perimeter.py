class Solution:
    def islandPerimeter(self, grid: list[list[int]]) -> int:
        
        #for a particular land cell check its neighbors
        #check all four directions
        #if any of the 4 directions, if its water/ out of boundary then we can include
        ans=0

        m,n= len(grid), len(grid[0])
        visited= [ [0]*n for _ in range(m)]
        ans=0
        dir = [(1,0), (0,1), (-1,0), (0,-1)]
        def traverse(r,c):
            nonlocal ans
            visited[r][c]=1
            #for this cell check how many perimeter
            perimeter= 0 

        
            for d in dir:
                a,b =d
                new_r, new_c =a+r, b+c
                if not(0<=new_r<m) or not (0<=new_c<n):
                    #this is out of bound
                    perimeter+=1
                elif grid[new_r][new_c] ==0:
                    perimeter+=1
                
                if 0<=new_r<m and 0<=new_c<n and not visited[new_r][new_c] and grid[new_r][new_c]:
                    #this is a land
                    traverse(new_r, new_c)
            ans+=perimeter
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    traverse(i,j)
                    
        return ans


