class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """
        append max(starts), min(ends)
        also move the ptr for the interval that ends earlier
        basically among 2 intervals the one ending late can ovralp with any start
        """
        answer=[]
        n1 = len(firstList)
        n2 = len(secondList)
        i,j=0,0
        while i<n1 and j<n2:
            start= max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start<=end:
                answer.append([start, end])
            
            if secondList[j][1]>= firstList[i][1]:
                #move the one that ends earlier
                i+=1
            else:
                j+=1
        return answer
