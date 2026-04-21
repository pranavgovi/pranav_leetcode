class Solution:
    def minimumHammingDistance(self, source: List[int], target: List[int], allowedSwaps: List[List[int]]) -> int:
        neighbors=defaultdict(list)
        n=len(allowedSwaps)
        lookup={}
        for i in range(n):
            a,b= allowedSwaps[i] 
            srca = source[a]
            srcb =source[b]
            neighbors[srca].append(srcb)
            neighbors[srcb].append(srca)

        def dfs(node, flag):
            lookup[node]= flag
            for neighbor in neighbors[node]:
                if neighbor not in lookup:
                    dfs(neighbor, flag)
        ans=0
        n=len(source)
    
        ptr=1
        for node in source:
            if node not in lookup:
                dfs(node,ptr)
                ptr+=1
        ans=0
        print(lookup)
        for i in range(n):
            if target[i] not in lookup:
                ans+=1
            elif source[i]==target[i]:
                continue
            else:
                if lookup[source[i]]!=lookup[target[i]]:
                    ans+=1
        return ans




        
