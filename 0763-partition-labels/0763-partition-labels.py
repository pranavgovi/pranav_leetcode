class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lookup=defaultdict(int)
        n=len(s)
        for ind, val in enumerate(s):
            lookup[val] = ind
        
        #this lookup will have the farthest indices of the chrs in s
        answer=[]
        i=0
        while i<n:
            farthest = lookup[s[i]]
            t=i
            while i<=farthest and farthest<n:
                farthest = max(farthest, lookup[s[i]])
                i+=1
            answer.append(farthest-t+1)
            i=farthest+1
        return answer
        

            


