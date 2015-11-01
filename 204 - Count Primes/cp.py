import math

class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        is_prime = [1] * (n + 1)
        for p in range(2, int(math.sqrt(n)) + 1):
            if is_prime[p] == 1
                for idx in range(p * p, n + 1, p):
                    is_prime[idx] = 0
        
        return sum(is_prime) - 1
