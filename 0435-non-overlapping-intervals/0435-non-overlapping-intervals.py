class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        first I am trying to think when 2 intervals overlap which one should we remove, 
        among the two the one that ends quickly so it has less chances of overlapping
        """
        intervals.sort()
        removals = 0
        prev_start, prev_end = intervals[0]
        n = len(intervals)
        for i in range(1,n):
            curr_start, curr_end = intervals[i]
            if prev_end <= curr_start:
                prev_start, prev_end = curr_start, curr_end
                continue
            
            else:
                removals+=1
                prev_end = min(curr_end, prev_end)
        return removals
