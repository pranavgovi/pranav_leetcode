class Solution:
    def getSum(self, a: int, b: int) -> int:
        max_int = 0x7fffffff
        mask = 0xffffffff
        a = a&mask #to keep just 32 bits
        b =b &mask
        answer=0
        carry=0
        pos=0
        
        while a or b or carry:
        #left shift to make spcae
            bit1= a&1
            a=a>>1 #extract bit and right shift
            bit2= b&1
            b=b>>1 #extarct bit and rihgt shift
            value = bit1 ^ bit2^carry
            carry = (bit1&bit2) | (bit2& carry) | (bit1& carry)
            answer = answer | (value<<pos)
            pos+=1
        answer= answer&mask

        if answer<max_int:
            return answer
        return answer- (2**32)