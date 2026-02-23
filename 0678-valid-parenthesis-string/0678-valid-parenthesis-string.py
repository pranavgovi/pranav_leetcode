class Solution:
    def checkValidString(self, s: str) -> bool:
        left=0
        right=0
        star=0
        #left traversal
        for i in s:
            if i=='(':
                left+=1
            elif i==')':
                right+=1
            else:
                star+=1
            if right-left>0:
                #this means that close is greater than open
                #i have to use a star
                if not star:
                    return False
                star-=1
                left+=1
                
        n=len(s)
        left,right,star=0,0,0
        for i in range(n-1,-1,-1):
            if s[i]==')':
                right+=1
            elif s[i]=='(':
                if right>0:
                    right-=1
                elif star>0:
                    star-=1
                else:
                    return False
            else:
                star+=1
        return True
        

        