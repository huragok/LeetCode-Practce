class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        
        for f in [2, 3, 5]:
            while num % f == 0:
                num /= f
        return num == 1
