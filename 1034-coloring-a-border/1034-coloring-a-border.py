class Solution:
    def colorBorder(self, grid: list[list[int]], row: int, col: int, color: int) -> list[list[int]]:
        """
        start with grid cell (row, col) do a dfs and identify all connected components
        #they can be simply marked visited
        #what makes a cell border??
        #if it has atleast one neighbor not of the component or it is at the top/bottom row/col
        """
        borders =set()
        dir = [(1,0), (0,1), (-1,0), (0,-1)]

        m,n = len(grid), len(grid[0])
        visited = [ [0]*n for _ in range(m)]
        def traverse(r,c):
            visited[r][c]=1

            border = False

            for d in dir:
                a,b = d
                new_r, new_c = a+r, b+c
                if new_r<0 or new_r>=m or new_c<0 or new_c>=n:
                    border= True
                    
                elif grid[new_r][new_c]!= grid[r][c]:
                    border= True
                if 0<=new_r<m and 0<=new_c<n and grid[r][c]==grid[new_r][new_c] and not visited[new_r][new_c]:
                    traverse(new_r, new_c)
            if border:
                borders.add((r,c))
        traverse(row, col)

        for x in borders:
            a,b =x
            grid[a][b]= color
        return grid

