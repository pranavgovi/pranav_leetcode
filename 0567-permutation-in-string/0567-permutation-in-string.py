class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #this is a fixed window variant

        needed ={}
        having ={}
        have=0
        for i in s1:
            if i not in needed:
                needed[i]=1
            else:
                needed[i]+=1
        
        left=0
        for right in range(len(s2)):

            if s2[right] not in needed:
                #we dont need this char
                have=0
                having ={}
                left=right+1
            
            else:

                having[s2[right]]  = having.get(s2[right], 0) + 1

                if having[s2[right]] == needed[s2[right]]:
                    have+=1
                

                while right-left+1 > len(s1):
                    #this exceeds the length

                    #move left
                    if s2[left] in having:
                        if having[s2[left]] == needed[s2[left]]:
                            have-=1
                        having[s2[left]]-=1
                    left+=1

                if right-left+1 == len(s1) and have == len(needed):
                    return True
        
            
        return False
        

    

