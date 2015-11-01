class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return k
        else:
            a = k
            b = k * (k - 1)
            
            for idx in xrange(2, n):
                a, b = b, (k - 1) * (a + b)
                
            return a + b
