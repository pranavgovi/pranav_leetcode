class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.sort()

        answer=[]
        i=0
        n=len(intervals)
        #ending is less than newInterval starting
        while i<n and intervals[i][1]< newInterval[0]:
            answer.append(intervals[i])
            i+=1
      
        #now there is a merging interval at i
        #perform merging till u see an interval whose interval[i][0]> curr_end
        curr_start, curr_end = newInterval[0], newInterval[1]
        while i<n and intervals[i][0] <= curr_end:

            curr_start = min(intervals[i][0], curr_start)
            curr_end = max(intervals[i][1], curr_end)
            i+=1
        
        answer.append([curr_start, curr_end])

        while i<n:
            answer.append(intervals[i])
            i+=1
        return answer