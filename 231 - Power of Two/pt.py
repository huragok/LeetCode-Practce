class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            if n % 2 == 1:
                return False
            n >>= 1
            
        return True
