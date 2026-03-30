class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        answer=[]
        intervals.sort(key = lambda interval: (interval[0], interval[1]) )
        prev_start, prev_end = intervals[0][0], intervals[0][1]

        for i in range(1,n):
            curr_start, curr_end = intervals[i][0], intervals[i][1]
            if curr_start>prev_end:
                #no overlap
                #we can append the (prev) to the answer
                answer.append([prev_start, prev_end])
                prev_start, prev_end= curr_start, curr_end
            
            else:
                prev_end = max(prev_end, curr_end)
        answer.append([prev_start, prev_end])
        return answer