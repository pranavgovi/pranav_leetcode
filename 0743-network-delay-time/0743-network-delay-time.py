class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #we have to make sure we reach all the nodes in shortest time possible return the maximum of the times
        min_heap=[]
        heapq.heappush(min_heap, (0,k)) #we start at k where t=0
        neighbors=defaultdict(list)
        for node in times:
            src, dest, time =node
            neighbors[src].append([dest, time]) 

        visited=set()
        ans=0
        while min_heap:
            t , node= heapq.heappop(min_heap)
            if node in visited:
                continue
            ans=max(ans, t)
            visited.add(node)
            for nei in neighbors[node]:
                nd , time_taken =nei
                if nd not in visited:
                    heapq.heappush(min_heap,(t+time_taken, nd) )
        
        if len(visited)!=n:
            return -1
        return ans
        
            #while pushing neighbors 