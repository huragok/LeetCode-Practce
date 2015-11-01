class Vector2D(object):

    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.vec = []
        for l in vec2d:
            self.vec += l
        self.n = len(self.vec)
        self.idx = -1

    def next(self):
        """
        :rtype: int
        """
        self.idx += 1
        return self.vec[self.idx]
        

    def hasNext(self):
        """
        :rtype: bool
        """
        return self.idx + 1 < self.n
        

if __name__ == "__main__":
    vec2d = [
              [1,2],
              [3],
              [4,5,6]
            ]
    # Your Vector2D object will be instantiated and called as such:
    i, v = Vector2D(vec2d), []
    while i.hasNext(): v.append(i.next())
    print(v)
