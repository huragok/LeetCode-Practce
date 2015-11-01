import math

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        
        n_shift = (m ^ n).bit_length()
        return ((m & n) >> n_shift) << n_shift
        
        
if __name__ == "__main__":
    m = 5
    n = 5
    print(Solution().rangeBitwiseAnd(m, n))
        
