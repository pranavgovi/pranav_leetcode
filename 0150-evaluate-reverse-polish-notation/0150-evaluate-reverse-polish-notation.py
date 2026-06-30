class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ans=0
        stack=[]
        op = {'+', '-', '*', '/'}
        for token in tokens:

            stack.append(token)
            while len(stack)>2 and stack[-1] in op and stack[-2] not in op and stack[-3] not in op:
                operation= stack.pop()
                value2 = int(stack.pop())
                value1 = int(stack.pop())
                if operation=='+':
                    stack.append(value1+ value2)
                elif operation=='-':
                    stack.append(value1-value2)
                elif operation=='*':
                    stack.append(value1*value2)
                else:
                    stack.append(value1/value2)
        return int(stack[0])
                    
        