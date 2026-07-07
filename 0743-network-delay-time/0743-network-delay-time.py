class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        from collections import deque, defaultdict
        """
        task is to obtain the maximum of all minimum time it takes for the signal to reach every node
        """
        INF =float('inf')
        maxi = 0
        min_time = [INF]*(n+1)
        queue= deque()
        neighbors=defaultdict(list)
        for time in times:
            source, dest, t = time
            neighbors[source].append((dest, t))
        
        queue.append((k, 0))
        min_time[k]=0
        #so queue consists of node, time_taken to reach node from source


        while queue:
            node, node_time = queue.popleft()
            min_time[node] = min(min_time[node],node_time)
            for nei in neighbors[node]:
                nei_node, nei_time = nei
                #append a node only when it can be reached faster than its prev value
                if min_time[nei_node] > nei_time+node_time:
                    queue.append((nei_node, nei_time+ node_time))
    
        answer=0
        for i in range(1,n+1):
            if min_time[i]==INF:
                return -1
            else:
                answer= max(answer, min_time[i])
        return answer

            