class MinStack:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []
        self.stack_min = []
        

    # @param x, an integer
    # @return nothing
    def push(self, x):
        self.stack.append(x)
        if not self.stack_min and self.stack_min[-1] < x:
            self.stack_min.append(self.stack_min[-1])
        else:
            self.stack_min.append(x)
        

    # @return nothing
    def pop(self):
        if self.stack_min:
            self.stack_min.pop()
        return self.stack.pop()
        

    # @return an integer
    def top(self):
        return self.stack[-1]
        

    # @return an integer
    def getMin(self):
        return self.stack_min[-1]
