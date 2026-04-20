class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        #multi source bfs
        answer= [[0]*m for _ in range(n)]
        queue=deque()
        visited = set()
        for src in sources:
            a,b,c = src
            queue.append((a,b,c))
            visited.add((a,b))
            answer[a][b] =c

        directions = [(1,0),(0,1), (-1,0), (0,-1)]
 
        while queue:
            x=len(queue) 
            first_time_seen= {}
            for i in range(x):
                a,b,c = queue.popleft()
                #for (a,b) we can go over the neighbors and 
          
                for dir in directions:
                    x,y = dir
                    new_r, new_c = x+a, y+b
                    if 0<=new_r<n and 0<=new_c<m and (not answer[new_r][new_c] or (new_r, new_c) in first_time_seen):
                        answer[new_r][new_c]= max(answer[new_r][new_c], c)
                        first_time_seen[(new_r, new_c)] = answer[new_r][new_c]
                        if (new_r, new_c) not in visited:
                            visited.add((new_r, new_c))
                            queue.append((new_r, new_c,answer[new_r][new_c]))
                
                for key, val in first_time_seen.items():
                    row, col = key
                    answer[row][col]= val
            
                
            #now current level's  neighbors are poppulated with ther max valurs
            #add them to queue
      
        return answer
                
                



            
            
            