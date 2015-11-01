import math

class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        p = int(math.sqrt(n))
        if p ** 2 == n:
            return 1
        
        while (n & 3 == 0):
            n >>= 2
        if n & 7 == 7:
            return 4
            
        #print(p)
        p = int(math.sqrt(n))
        for i in xrange(1, p + 1):
            m = n - i ** 2
            print(m)
            q = int(math.sqrt(m))
            if q ** 2 == m:
                return 2
                
        return 3
        
        
if __name__ == "__main__":
    n = 12
    print(Solution().numSquares(n))
            
