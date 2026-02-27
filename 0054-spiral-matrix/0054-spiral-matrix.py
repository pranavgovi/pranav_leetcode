class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        #top can range from 0 -> len(matrix)-1
        #bottm len(matrix)-1 towrads top
        #top should always be < bottom
        #left ranges from 0 -> n(columns)-1
        #right -> vice versa
        #left should alwyas < right
        answer=[]
        m,n = len(matrix), len(matrix[0])
        top, left = 0, 0
        bottom, right = m-1, n-1
        while top<=bottom and left<=right:
            #process left to right and inc top
            for i in range(left, right+1):
                answer.append(matrix[top][i])
            top+=1
            #now process top to bottom and inc right

            for i in range(top, bottom+1):
                answer.append(matrix[i][right])
            right-=1

            #now process right to left and decrease bottom
            #to not process same top, bootm
            if top<=bottom:
                for i in range(right, left-1, -1):
                    answer.append(matrix[bottom][i])
                
                bottom-=1
            #proces bottom to top and move left
            if left<=right:
                for i in range(bottom, top-1, -1):
                    answer.append(matrix[i][left])
                left+=1
        return answer




