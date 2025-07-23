class MinStack:

    def __init__(self):
        self.stack=[]
        self.mini=float('inf')

    def push(self, val: int) -> None:
        if not self.stack:
            self.mini=val
            self.stack.append(val)
        else:
            if val<self.mini:
                self.stack.append(2*val-self.mini)
                self.mini=val
            else:
                self.stack.append(val)

    def pop(self) -> None:
        if not self.stack:
            return mini
        top=self.stack.pop()
        if top<self.mini:
            self.mini=2*self.mini-top

    def top(self) -> int:
        top=self.stack[-1]
        if top<self.mini:
            return self.mini
        return top

    def getMin(self) -> int:
        return self.mini


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()