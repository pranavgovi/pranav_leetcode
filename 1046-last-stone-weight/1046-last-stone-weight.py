class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap=[]
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        heapq.heapify(max_heap)
        while len(max_heap)>=2:
            stone1= -1*heapq.heappop(max_heap)
            stone2 = -1*heapq.heappop(max_heap)
            if stone1==stone2:
                continue
            else:
                heapq.heappush(max_heap, -(abs(stone1-stone2)))
        if max_heap:
            return -max_heap[0]
        return 0

