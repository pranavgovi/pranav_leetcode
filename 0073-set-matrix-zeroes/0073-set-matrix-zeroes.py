class Solution:
    def setZeroes(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row0= 1
        col0=1
        m,n =len(arr), len(arr[0])
        for i in range(m):
            for j in range(n):
                if arr[i][j]==0:
                    if i==0 and j==0:
                        row0=0
                        col0=0
                    
                    elif i==0:
                        row0=0
                        arr[0][j]=0
                    elif j==0:
                        col0=0
                        arr[i][0]=0
                    else:
                        arr[i][0]=0
                        arr[0][j]=0
            
        for i in range(1,m):
            if arr[i][0]==0:
                for j in range(n):
                    arr[i][j]=0
        
        for j in range(1,n):
            if arr[0][j]==0:
                for i in range(m):
                    arr[i][j]=0
        
        if row0==0:
            for j in range(n):
                arr[0][j]=0
        if col0==0:
            for i in range(m):
                arr[i][0]=0




                    

                    
                        
                    
                        #update the shared state
                        
                
        