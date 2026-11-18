class Solution:
    def minChanges(self, s: str) -> int:
        
        arr= list(s)
        n=len(s)
        cnt=0
        i=0
        while i<n-1:
            if arr[i]==arr[i+1]:
                i+=2
            else:
                arr[i+1]=arr[i]
                i+=2
                cnt+=1
        return cnt