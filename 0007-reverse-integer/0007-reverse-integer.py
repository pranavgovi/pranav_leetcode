class Solution:
    def reverse(self, x: int) -> int:
        MAX, MIN = (2**31)-1, -(2**31)
        neg=False
        if x<0:
            neg= True
        
        answer =0 
    
        while x:
            curr_digit = int(math.fmod(x, 10)) #for negative numbers also int is used becuase float can be returned
            if answer>int(MAX/10) or (answer==int(MAX/10) and curr_digit>7):
                return 0
            if answer<int(MIN/10) or answer==int(MIN/10) and curr_digit<-8:
                return 0
            #before building the answer check
            #now builidng the answer
            answer= answer*(10) + curr_digit
            x=int(x/10) #x//10 will truncate towars -inf
        return answer
       