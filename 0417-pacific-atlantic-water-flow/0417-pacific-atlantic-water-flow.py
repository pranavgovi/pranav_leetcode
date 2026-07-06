class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m,n = len(heights), len(heights[0])
        pacific_queue=deque()
        atlantic_queue = deque()
        pacific_visited=[[0]*n for i in range(m)]
        atlantic_visited = [ [0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0 or j==0:
                    pacific_visited[i][j]=1
                    pacific_queue.append((i,j))
                if i==m-1 or j==n-1:
                    atlantic_visited[i][j]=1
                    atlantic_queue.append((i,j))
        directions =[(1,0), (0,1), (-1,0), (0,-1)]
        def traverse(visited, queue):

            while queue:
                r,c = queue.popleft()
                for dir in directions:
                    a,b = dir
                    new_r, new_c = r+a, c+b
                    if 0<=new_r<m and 0<=new_c<n and heights[new_r][new_c]>= heights[r][c] and not visited[new_r][new_c]:
                        queue.append((new_r, new_c))
                        visited[new_r][new_c]=1
        traverse(pacific_visited, pacific_queue)
        traverse(atlantic_visited, atlantic_queue)
        ans=[]
        for i in range(m):
            for j in range(n):
                if pacific_visited[i][j] and atlantic_visited[i][j]:
                    ans.append((i,j))
        return ans
