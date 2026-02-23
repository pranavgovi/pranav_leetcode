class Solution:
    def checkValidString(self, s: str) -> bool:
        
        star =0
        o,c = 0,0
        for i in s:
            if i=='(':
                o+=1
            elif i=='*':
                star+=1
            else:
                if o:
                    o-=1
                elif star:
                    star-=1
                else:
                    #nothing is there
                    return False
        c=0
        start=0
        for i in range(len(s)-1,-1,-1):
            if s[i]==')':
                c+=1
            elif s[i]=='*':
                star+=1
            else:
                if c:
                    c-=1
                elif star:
                    star-=1
                else:
                    #nothing is there
                    return False
     
        return True
            

        
    