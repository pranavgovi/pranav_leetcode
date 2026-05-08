class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:

        def generate(arr):
            n=len(arr)
            for i in range(n-1,-1,-1):
                if arr[i]=='#':
                    #check if it can go further
                    while i+1<n and arr[i+1]=='.':
                        #swap both
                        arr[i], arr[i+1] = arr[i+1], arr[i]
                        i+=1
        answer=[]
        for grid in boxGrid:
            generate(grid)
            answer.append(grid)
        m=len(boxGrid) #2
        n=len(boxGrid[0]) #4
        final=[]
        for i in range(n):
            arr=[]
            for j in range(m-1,-1,-1):
                arr.append(answer[j][i])
            final.append(arr)
        return final
        


