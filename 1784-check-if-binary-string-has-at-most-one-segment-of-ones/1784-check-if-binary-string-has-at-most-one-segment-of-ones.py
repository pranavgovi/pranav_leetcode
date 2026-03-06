class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        
        prev_one= -1
        for i in range(len(s)):

            if s[i]=='1':
                if prev_one==-1:
                    #I am seeing the first one
                    prev_one=i
                
                else:
                    #i have seen a one somewhere
                    if prev_one!=i-1:
                        return False
                    
                    else:
                        #update
                        prev_one=i
        return True
        
