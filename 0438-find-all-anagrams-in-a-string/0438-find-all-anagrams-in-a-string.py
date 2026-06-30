class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(s)<len(p):
            return []
        answer=[]
        having={}
        needed={}
        for i in p:
            if i not in needed:
                needed[i]=1
            else:
                needed[i]+=1
        n=len(s)
        left, right=0,0
        while left<=right and right<n:
            if s[right] not in needed:
                #jump back
                right+=1
                left=right
                having={}
            
            else:
                #this character is needed , simply include it
                if s[right] not in having:
                    having[s[right]]=1
                else:
                    having[s[right]]+=1
                
                while right-left+1 > len(p):
                    if s[left] in having:
                        having[s[left]]-=1
                    left+=1
                
                if needed==having:
                    answer.append(left)
                right+=1
        return answer