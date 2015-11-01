class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        num_list = map(int, str(num))
        while len(num_list) > 1:
            num = sum(num_list)
            num_list = map(int, str(num))
            
        return num
