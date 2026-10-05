class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        total_score=0
        stack=[]

        i=0
        n=len(s)
        while i<n:
            if s[i]=='(':
                stack.append('(')
            else:
                #this is a closed string
                #trace back and see if there are any values in stack
                score= 0
                while stack and stack[-1]!='(':
                    score+= stack[-1]
                    stack.pop()
                if stack:
                    stack.pop() #u remove the open bracket and add the score
                if not score:
                    #it means it has no values in between
                    stack.append(1)
                else:
                    stack.append(2*score)
            i+=1
        
        return sum(stack)