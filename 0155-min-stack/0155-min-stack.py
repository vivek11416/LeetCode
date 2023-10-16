class MinStack:

    def __init__(self):
        self.items = []
        self.min = []
        

    def push(self, val: int) -> None:
        if not self.items:
            self.items.append(val)
            self.min.append(val)
            
        elif val>= self.min[-1]:
            self.min.append(self.min[-1])
            self.items.append(val)
        else:
            self.min.append(val)
            self.items.append(val)
            
           
    def pop(self) -> None:
        self.items.pop()
        self.min.pop()
        

    def top(self) -> int:
        return self.items[-1]
        

    def getMin(self) -> int:
        return self.min[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()