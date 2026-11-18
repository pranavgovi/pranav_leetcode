class Solution:
    def sumCounts(self, s: List[int]) -> int:
        n=len(s)
        ans=0
        for i in range(n):
            seen=set()
            seen.add(s[i])
            ans+=1
            for j in range(i+1,n):
                seen.add(s[j])
                ans+=(len(seen)**2)
        return ans

       
