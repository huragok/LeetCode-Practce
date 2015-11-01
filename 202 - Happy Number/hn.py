class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        history = {}
        
        while n not in history and n != 1:
            history.add(n)
            digits = map(int, str(n))
            n = sum([d ** 2 for d in digits])
            
        return n == 1
