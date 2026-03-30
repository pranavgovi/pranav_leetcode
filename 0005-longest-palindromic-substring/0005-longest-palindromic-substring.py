class Solution:
    def longestPalindrome(self, name: str) -> str:
        
        n=len(name)
        max_len =float('-inf')
        max_str=''

        def check_pal(left, right): #O(n)
            nonlocal max_len
            nonlocal max_str
            while left>=0 and right<n and name[left]==name[right]:
                if right-left+1>max_len:
                    max_len=right-left+1
                    max_str=name[left:right+1]
                left-=1
                right+=1
                
            
            return

        #each chr in s consider it to be center of odd length and even length pal 
        #O(n**3)
        for i in range(n):
            #odd_length
            check_pal(i,i)
            if i+1<n:
                check_pal(i, i+1)
        return max_str