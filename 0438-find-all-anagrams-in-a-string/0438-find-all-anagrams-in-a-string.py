class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        needed = {}
        answer=[]
        for i in p:
            if i not in needed:
                needed[i]=1
            else:
                needed[i]+=1
        
        having ={}
        have =0 

        n = len(s)
        left, right = 0, 0

        while left <= right and right<n:

            if s[right] in needed:
                having[s[right]] = having.get(s[right], 0) +1
                
                if having[s[right]] == needed[s[right]]:
                    have+=1
              
    
            while right-left+1 > len(p) and left<=right:

                #try to move left
                if s[left] in needed:
                    #tweak the having because we r not storing unneccessary values in having
                    if having[s[left]] == needed[s[left]]:
                        have-=1
                    having[s[left]]-=1
                        #will there be any issue if we ddont remove s[left] from having when it reaches 
                left+=1
            if have == len(needed) and right-left+1 ==len(p):
                answer.append(left)
            right+=1
        return answer