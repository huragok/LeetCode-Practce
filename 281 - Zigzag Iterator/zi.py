class ZigzagIterator(object):

    def __init__(self, v1, v2):
        """
        Initialize your data structure here.
        :type v1: List[int]
        :type v2: List[int]
        """
        self.v = [v1, v2]
        self.n = [len(v1), len(v2)]
        self.row = 1
        self.col = -1

    def next(self):
        """
        :rtype: int
        """
        if self.row == 1:
            self.row = 0 if self.col + 1 < self.n[0] else 1
            self.col += 1
        else:
            if self.col < self.n[1]:
                self.row = 1
            else:
                self.col += 1
        return self.v[self.row][self.col]

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.row == 1:
            if self.col + 1 < self.n[0]:
                row_next = 0
                col_next = self.col + 1
            else:
                row_next = 1
                col_next = self.col + 1
        else:
            if self.col < self.n[1]:
                row_next = 1
                col_next = self.col
            else:
                row_next = 0
                col_next = self.col + 1
            
        return col_next < self.n[row_next]

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
