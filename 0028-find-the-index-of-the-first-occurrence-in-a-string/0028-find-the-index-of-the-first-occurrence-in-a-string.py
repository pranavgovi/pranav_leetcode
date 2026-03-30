class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        left=0
        n1=len(needle)
        n=len(haystack)
        while left<n:
            i=0
            start=left
            while left<n and i<n1 and haystack[left]==needle[i]:
                left+=1
                i+=1
            if i==n1:
                return start
            left= start+1
        
        return -1

            

            