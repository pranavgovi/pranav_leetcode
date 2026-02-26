class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        n=len(intervals)
        removal=0
        a,b = intervals[0][0], intervals[0][1]
        for i in range(1,n):
            c,d = intervals[i][0], intervals[i][1]
            if c<b:
                #if they are overallppi g try removing the one that ends the last
                removal+=1
                if b>d:
                    a,b = c,d
            else:
                #no overlap just chnage
                a,b = c,d
        return removal