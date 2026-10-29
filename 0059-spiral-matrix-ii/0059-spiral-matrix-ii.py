class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        
        answer = [ [0]*n for _ in range(n)]

        top, left=0,0
        bottom , right= n-1,n-1
        i=1
        while top<=bottom and left<=right:
            #first process the top

            for j in range(left, right+1):
                answer[top][j] = i
                i+=1
            
            top+=1
            for row in range(top, bottom+1):
                answer[row][right]= i
                i+=1
            
            right-=1

            if top<=bottom and left<=right:

                for col in range(right, left-1,-1):
                    answer[bottom][col]=i
                    i+=1
                
                bottom-=1

                for row in range(bottom, top-1,-1):
                    answer[row][left]=i
                    i+=1
                
                left+=1
        return answer