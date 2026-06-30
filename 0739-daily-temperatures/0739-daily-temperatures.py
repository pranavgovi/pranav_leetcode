class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #find the index of next greater element j so ans is j-i

        stack = []
        n=len(temperatures)
        answer=[0]*n
        for i in range(n-1,-1,-1):
            
            while stack and temperatures[stack[-1]]<=temperatures[i]:
                stack.pop()
            if stack:
                answer[i]= stack[-1]-i
            stack.append(i)
        return answer