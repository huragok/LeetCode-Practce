import re

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        s = re.split(r'(\d+|\W+)', s)
        print(s)
        
if __name__ == "__main__":
    s = " 2-1 + 2 "
    Solution().calculate(s)
