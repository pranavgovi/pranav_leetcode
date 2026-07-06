class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        queue=deque()
        m,n= len(board), len(board[0])

        directions =[(1,0), (0,1), (-1,0), (0,-1)]
        
        for i in range(m):
            for j in range(n):
                if (i==0 or i==m-1 or j==n-1 or j==0) and (board[i][j]=='O'):
                    queue.append((i,j))
                    board[i][j]='S'
        
        while queue:
            r,c= queue.popleft()
            for dir in directions:
                a,b = dir
                new_r, new_c = a+r,b+c
                if 0<=new_r<m and 0<=new_c<n and board[new_r][new_c]=='O':
                    queue.append((new_r, new_c))
                    board[new_r][new_c]='S'
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='S':
                    board[i][j]='O'
                elif board[i][j]=='O':
                    board[i][j] = 'X'