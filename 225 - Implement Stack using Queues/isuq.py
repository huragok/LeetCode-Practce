class Stack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.queue1 = []
        self.queue2 = []
        self.count = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.queue1.append(x)
        self.count += 1
        

    def pop(self):
        """
        :rtype: nothing
        """
        for n in xrange(self.count - 1):
            self.queue2.append(self.queue1.pop(0))
        self.count -= 1
        tmp = self.queue1.pop(0)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return tmp


    def top(self):
        """
        :rtype: int
        """
        for n in xrange(self.count):
            x = self.queue1.pop(0)
            self.queue2.append(x)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return x
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.count == 0
        
