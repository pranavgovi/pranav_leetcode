class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        outdegree=[0]*numCourses
        n=numCourses
        lookup=defaultdict(list)
        for pre in prerequisites:
            a,b =pre
            outdegree[a]+=1
            lookup[a].append(b)
            lookup[b].append(a)
        queue=deque()
        ans=[]
        # visited=[0]*n
        for i in range(n):
            if not outdegree[i]:
                queue.append(i)
     
            
        
        while queue:
            node = queue.popleft()
            ans.append(node)
            for nei in lookup[node]:
                outdegree[nei]-=1
                if not outdegree[nei]:
                    queue.append(nei)
        if len(ans)!=n:
            return False
        return True
            
