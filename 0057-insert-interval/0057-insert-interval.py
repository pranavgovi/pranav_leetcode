class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort()
        answer=[[intervals[0][0], intervals[0][1]]]
        n=len(intervals)
        for i in range(1,n):
            a,b = answer[-1][0], answer[-1][1]
            c,d = intervals[i][0], intervals[i][1]
            if b>=c:
                answer.pop()
                answer.append([a, max(b,d)])
            else:
                answer.append(intervals[i])
        return answer

            
            
            