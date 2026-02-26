class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        answer=[]
        intervals.sort()
        n=len(intervals)
        a,b = intervals[0][0], intervals[0][1]
        for i in range(1,n):
            c,d = intervals[i][0], intervals[i][1]
            if b>=c:
                #overlap
                a,b =a , max(b,d)
            else:
                #just append
                answer.append([a,b])
                a,b = c,d
        answer.append([a,b])
        return answer

