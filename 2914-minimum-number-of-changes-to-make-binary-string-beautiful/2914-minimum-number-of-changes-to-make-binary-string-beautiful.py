class Solution:
    def minChanges(self, arr: str) -> int:
        

        n=len(arr)
        cnt=0
        i=0
        while i<n-1:
            if arr[i]==arr[i+1]:
                i+=2
            else:
                
                i+=2
                cnt+=1
        return cnt