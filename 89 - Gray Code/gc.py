class Solution:
    # @param {integer} n
    # @return {integer[]}
    def grayCode(self, n):
        return self._grayCode(n)
        
    def _grayCode(self, n):
        if n == 0:
            return []
        elif n == 1:
            return [0, 1]
        else:
            gc_rest = self._grayCode(n - 1)
            a = 2 ** (n - 1)
            return gc_rest + [a + n for n in reversed(gc_rest)]
            
if __name__ == "__main__":
    n = 2
    print(Solution().grayCode(n))
