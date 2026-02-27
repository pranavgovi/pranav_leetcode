class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m,n=len(matrix), len(matrix[0])
        for i in range(m):
            for j in range(n):
                if i<j and i!=j:
                    matrix[i][j], matrix[j][i]= matrix[j][i], matrix[i][j]
        print(matrix)

        #in place reverse
        def reverseFun(arr):
            n=len(arr)
            for i in range(n//2):
                arr[i], arr[n-i-1]= arr[n-i-1], arr[i]
            
        for i in range(m):
            reverseFun(matrix[i])
