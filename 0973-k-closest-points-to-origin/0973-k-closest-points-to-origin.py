class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import heapq
        max_heap=[]
        for i,point in enumerate(points):
            a,b=point
            dist= a**2 + b**2
            heapq.heappush(max_heap, (-dist, i))
            if len(max_heap)>k:
                heapq.heappop(max_heap)
        ans=[]
        for i in max_heap:
            _, index = i
            ans.append(points[index])
        return ans

