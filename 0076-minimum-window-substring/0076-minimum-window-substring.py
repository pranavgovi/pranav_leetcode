class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t)>len(s):
            return ""
        needed={}
        having={}
        
        have = 0
        for i in t:
            if i not in needed:
                needed[i]=1
            else:
                needed[i]+=1
        need= len(needed)
        left= 0
        right= 0
        ans= float('inf')
        ans_word=''
        n=len(s)
        while left<=right and right<n:

            if s[right] not in needed:
                #I dont want this string
                right+=1
            else:
                having[s[right]] = having.get(s[right],0)+1
                if having[s[right]] == needed[s[right]]:
                    have+=1
                while have == need and left<=right:
                    if right-left+1< ans:
                        ans= right-left+1
                        ans_word= s[left:right+1]
                    if s[left] not in needed:
                        left+=1
                    else:
                        having[s[left]]-=1
                        if having[s[left]]< needed[s[left]]:
                            have-=1
                        left+=1
                right+=1
        return ans_word



