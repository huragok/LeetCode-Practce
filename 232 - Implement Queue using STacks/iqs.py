class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack_push = []
        self.stack_pop = []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        if self.stack_pop:
            while len(self.stack_pop) > 0:
                self.stack_push.append(self.stack_pop.pop())
        
        self.stack_push.append(x)
        

    def pop(self):
        """
        :rtype: nothing
        """
        if self.stack_push:
            while len(self.stack_push) > 0:
                self.stack_pop.append(self.stack_push.pop())
        
        self.stack_pop.pop()
        

    def peek(self):
        """
        :rtype: int
        """
        if self.stack_push:
            while len(self.stack_push) > 0:
                self.stack_pop.append(self.stack_push.pop())
        
        return self.stack_pop[-1]
        

    def empty(self):
        """
        :rtype: bool
        """
        return bool(self.stack_push) and bool(self.stack_pop)
