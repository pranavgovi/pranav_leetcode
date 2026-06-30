class Solution:
    def isValid(self, s: str) -> bool:
        lookup={
            '{':'}', '[':']', '(':')'
        }
        stack=[]
        for i in s:
            if i in lookup:
                #it is a open
                stack.append(i)
            else:
                #it is a closed paranthesis
                if not stack:
                    return False
                if stack and lookup[stack[-1]]!=i:
                    return False
                stack.pop()
        if stack:
            return False
        return True