class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        from collections import deque
        timer =0
        cooldown = deque()
        lookup=defaultdict(int)
        for task in tasks:
            lookup[task]+=1
        
        max_heap =[]
        for key, value in lookup.items():
            heapq.heappush(max_heap, -value)
        
        timer = 0
        
        while max_heap or cooldown:
            if cooldown:
                if cooldown[0][0]<=timer:
                    heapq.heappush(max_heap, -cooldown[0][1]) #u r appending the freq
                    cooldown.popleft()
                
            if max_heap:
                freq = heapq.heappop(max_heap)
                freq+=1
                #now allot a cooldown
                if freq:
                    cooldown.append((timer+n+1, -freq))
            timer+=1
        return timer
        