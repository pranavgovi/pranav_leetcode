class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lookup={}
        left, right =0 , 0
        n=len(s)
        answer=0
        while left<=right and right<n:

            if s[right] not in lookup:
                #valid
                answer= max(answer, right-left+1)

                lookup[s[right]]=1
                right+=1
            
            else:
                #problem
                while s[left]!=s[right]:
                    #move left
                    del lookup[s[left]]
                    left+=1
                #now s[left]==s[right]
                left+=1
                
                #now I have removed
                #add s[right]
                right+=1
        return answer
                    
        