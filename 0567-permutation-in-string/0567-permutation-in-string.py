class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #this is a fixed window variant

        needed ={}
        having ={}

        for i in s1:
            if i not in needed:
                needed[i]=1
            else:
                needed[i]+=1
        
        left=0
        for right in range(len(s2)):

            if s2[right] not in needed:
                #we dont need this char
                left=right+1
                having={}
            else:

                having[s2[right]]  = having.get(s2[right], 0) + 1
                while right-left+1 > len(s1):
                    
                    if s2[left] in having:
                        having[s2[left]]-=1
                        
                    left+=1

                if needed== having:
                    return True
        
            
        return False
        

    

