class Solution:
    def canBeEqual(self, s1: str, s2: str) -> bool:
        ans= []
        n=4
        for i in range(4):
            if s1[i]==s2[i]:
                ans.append(s1[i])
            
            else:
                j = i+2
                if j>=n:
                    j=i-2
                    ans.append(s1[j])
                else:
                    ans.append(s1[j])
        if ''.join(ans)==s2:
            return True
        return False
                
