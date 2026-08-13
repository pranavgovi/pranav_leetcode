class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        
        base condition: l1+l2= l3
        (ind1, ind2) can we reach the end
        at each position we can either 
        1. include ind1 , exclude ind2
        2. exclude ind1, include ind2
        """
        memo={}
        l1, l2, l3  = len(s1), len(s2), len(s3)
        if l1+l2!=l3:
            return False
        def dp(ind1, ind2):
            if (ind1, ind2) in memo:
                return memo[(ind1, ind2)]
            #current index_state is obtained by ind1+ind2
            ind3= ind1+ind2
            if ind3==l3:
                memo[(ind1, ind2)]=True
                return True #we reached the end of the s3
            
            if ind1<l1 and ind2<l2:
                #none match
                if s1[ind1]!=s3[ind3] and s2[ind2]!=s3[ind3]:
                    memo[(ind1, ind2)]= False
           
                #both match
                elif s1[ind1]==s3[ind3] and  s2[ind2]==s3[ind3]:
                    memo[(ind1, ind2)] = dp(ind1+1, ind2) or dp(ind1, ind2+1)

                #atleast one match
                elif s1[ind1]==s3[ind3]:
                    memo[(ind1, ind2)] =  dp(ind1+1, ind2)
 
                else:
                    memo[(ind1, ind2)] = dp(ind1, ind2+1)
                return memo[(ind1, ind2)]
            elif ind1<l1:
                memo[(ind1, ind2)]= s1[ind1]==s3[ind3] and dp(ind1+1, ind2)
            else:
                memo[(ind1, ind2)] = s2[ind2]==s3[ind3] and dp(ind1, ind2+1)
            return memo[(ind1, ind2)]
        return dp(0,0)
                
