class Solution:
    def reverseWords(self, s: str) -> str:
        l= s.strip().split()
        ans=''
        l.reverse()
        for i in l:
            ans+=i
            ans+=' '
        return ans.strip()