class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        l=len(word)
        m,n= len(board), len(board[0])
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        visited= set()
        def search(r,c, ind):
            if ind == l-1:
                return True
            visited.add((r,c))
            for dir in directions:
                a,b =dir
                new_r, new_c = a+r, b+c
                if 0<=new_r<m and 0<=new_c<n and (new_r, new_c) not in visited and board[new_r][new_c] == word[ind+1]:
                    if search(new_r, new_c, ind+1):
                        return True
            visited.remove((r,c))
            return False
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if search(i,j, 0):
                        return True
        return False
                
            

