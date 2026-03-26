class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s2)
        n1=len(s1)
        if len(s1)>len(s2):
            return False
        needed=defaultdict(int)
        having={}
        for i in s1:
            needed[i]+=1
    
        in_hand=0
        left,right=0,0
        while left<=right and right<n:
            if s2[right] not in needed:
                right+=1
                left=right
                having={}
            else:
                if s2[right] not in having:
                    having[s2[right]]=0
                
                having[s2[right]]+=1
               
                if having[s2[right]]>needed[s2[right]]:
                    #move the left pointer till having==needed
                    while having[s2[right]]>needed[s2[right]]:
                        having[s2[left]]-=1
                        left+=1
                    
                
                if right-left+1==n1:
                    return True
                right+=1
                  
                            
        return False
            
        
        