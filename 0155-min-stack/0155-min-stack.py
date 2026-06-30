class MinStack:

    def __init__(self):
        self.array=[]
        self.stack=[]
        

    def push(self, value: int) -> None:
        self.array.append(value)
        
        if self.stack:
            if value>=self.stack[-1]:
                self.stack.append(self.stack[-1])
            else:
                self.stack.append(value)
        else:
            self.stack.append(value)

    def pop(self) -> None:
        self.stack.pop()
        self.array.pop()
        

    def top(self) -> int:
        return self.array[-1]
        

    def getMin(self) -> int:
        return self.stack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()