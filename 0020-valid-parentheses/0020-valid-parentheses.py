class Solution:
    def isValid(self, s: str) -> bool:
        lookup = {'{':'}', '[':']', '(':')'}
        stack=[]
        for i in s:
            if i not in lookup:
                #it is closed
                if not stack:
                    return False
                top =  stack[-1]
                if top not in lookup or lookup[top]!= i:
                    return False
                stack.pop()
            else:
                stack.append(i)
        if stack:
            return False
        else:
            return True
