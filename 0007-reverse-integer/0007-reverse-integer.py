class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = (2**31)-1, -(2**31)

        neg=False
        if x<0:
            neg= True
        x=abs(x)
        answer =0 
        
        while x:
            curr_digit = x%10
            x= x//10

            #now builidng the answer
            answer= answer*(10) + curr_digit
        if neg:
            answer=-answer

        if answer> MAX or answer<MIN:
            return 0
        else:
            return answer
            

