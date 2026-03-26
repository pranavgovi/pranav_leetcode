class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        
        def mul(a:str, b:str, zeros:int):

            n = len(a)
    
            answer = 0
            carry = 0
            k=0
            for i in range(n-1,-1,-1):
                val1 = ord(a[i]) - ord('0')
                val2 = ord(b)-ord('0')
                prod =val1*val2 + carry
                rem =prod%10
                carry = prod//10
                #construct with the remainder
                answer= answer+ rem*((10)**k)
                k+=1
            if carry:
                answer= answer+ carry*((10)**k)
            return answer* (10**zeros)

        n1 =len(num1)
        total=0
        zeros=0
        for i in range(n1-1,-1,-1):
            val = mul(num2,num1[i], zeros)
            zeros+=1
            total+=val



        return str(total)


