class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        """
        if arr[i][j]=1
        check if arr[]
        """
        m,n = len(mat), len(mat[0])
        
        #we can run a loop and mark the rows and columns with more than 1's
        row_lookup= defaultdict(int)
        col_lookup=defaultdict(int)
        for row in range(m):
            for col in range(n):
                if mat[row][col]==1:
                    row_lookup[row]+=1
                    col_lookup[col]+=1
        ans=0
        for r in range(m):
            for c in range(n):
                if mat[r][c]==1 and row_lookup[r]==1 and col_lookup[c]==1:
                    ans+=1
        return ans
