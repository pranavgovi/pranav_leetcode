class Solution:
    def reverse(self, x: int) -> int:
        
        sign = True
        if x<0:
            sign=False
            x*=-1
        
        elif x==0:
            return 0
        else:
            sign = True
        num=0
        
        while x:
            digit = x%10
            num = num*10 +digit
            x=x//10
        if sign:
            #positive num
            if num> (2**31-1):
                return 0
            else:
                return num
        else:
            if -num<(-(2**31)):
                return 0

            return -num