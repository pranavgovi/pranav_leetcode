class Solution:
    def myAtoi(self, s: str) -> int:
        #how to ignore / strip whitespace
        ans= s.lstrip()
        tot_length = len(ans)
        sign=''
        if tot_length==0:
            return 0
        if ans[0]=='-':
            sign='-'
            i=1
        elif ans[0]=='+':
            sign='+'
            i=1
        else:
            i=0
            sign='+'
        while i<tot_length and s[i]=='0':
            i+=1
        
        if i==tot_length:
            return 0
        tot=0
        
        while i<tot_length:
            if not ans[i].isdigit():
                break
            else:
                tot= int(ans[i]) + (tot*10)
                
                i+=1
        if sign=='-':
            if -tot<-2147483648:
                return -2147483648
            else:
                return -tot
        if tot>2147483647:
            return 2147483647
        else:
            return tot
