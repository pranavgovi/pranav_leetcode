class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        #basically we r gonna compute the shortest path for all nodes from start
        #the node with maximum time will be our total min overall

        neighbors=defaultdict(list)
        for time in times:
            source, target, distance = time
            neighbors[source].append((distance,target))
        
        myheap=[]
        heapq.heappush(myheap, (0,k))
        visited=set()

        ans = 0
        while len(visited)!=n and myheap:

            dist , node = heapq.heappop(myheap)
            ans=max(ans,dist)
            if not node in visited:
                visited.add(node)
                #while iterating through neighbors of node while pushing bACK ADD THIS DIST
                arr = neighbors[node]
                for neighbor in arr:
                    distance , neighbor_node=neighbor
                    heapq.heappush(myheap,(distance+dist , neighbor_node))
        
        if len(visited)!=n:
            return -1
        return ans
