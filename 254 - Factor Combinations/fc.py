import math
class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n == 1:
            return []
        self.factors = self.getListFactors(n)
        self.result = []
        self._getFactors(n, [])
        return self.result
        
    def _getFactors(self, n, fc_partial):
        if n == 1:
            self.result.append(fc_partial)
        for f in self.factors:
            if not fc_partial or fc_partial[-1] <= f and n % f == 0:
                self._getFactors(n / f, fc_partial + [f])
        return
        
    def getListFactors(self, n):
        factors = []
        for x in xrange(2, int(math.sqrt(n)) + 1):
            if n % x == 0:
                factors += [x, n / x]
               
        return set(factors)
        
if __name__ == "__main__":
    n = 1
    print(Solution().getFactors(n))
