class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (0,1), (-1,0), (0, -1)]
        m,n = len(heights), len(heights[0])
        def ocean_flow(visited, results, queue):
            while queue:
                x = len(queue)
                for i in range(x):
                    r,c = queue.popleft()
                    for dir in directions:
                        a,b =dir
                        new_r, new_c = a+r, b+c
                        if 0<=new_r<m and 0<=new_c<n and (new_r, new_c) not in visited and heights[new_r][new_c] >= heights[r][c]:
                            queue.append((new_r, new_c))
                            results[new_r][new_c]=1
                            visited.add((new_r, new_c))
                            #this means that from r,c -> new_r, new_c can be rewacjed
            return
        pacific_visited = set()
        atlantic_visited = set()
        pacific_results = [[0]*n for _ in range(m)]
        atlantic_results = [[0]*n for _ in range(m)]
        pacific_queue = deque()
        atlantic_queue = deque()
        for i in range(m):
            for j in range(n):
                if j==0 or i==0:
                    pacific_results[i][j]=1
                    pacific_queue.append((i,j))
                    pacific_visited.add((i,j))
                if i==m-1 or j==n-1:
                    atlantic_results[i][j]=1
                    atlantic_queue.append((i,j))
                    atlantic_visited.add((i,j))
        ocean_flow(pacific_visited, pacific_results, pacific_queue)
        ocean_flow(atlantic_visited, atlantic_results, atlantic_queue)
        answer=[]
        for i in range(m):
            for j in range(n):
                if pacific_results[i][j] and atlantic_results[i][j]:
                    answer.append([i,j])
        return answer

                


            #this function populates the results array denoting cells that can reach the ocean
