class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return []
        elif n == 1:
            return ['0', '1', '8']
        elif n == 2:
            return ["11","69","88","96"]
        else:
            upsidedown = {'1': '1', '6': '9', '8': '8', '9': '6'}
            return [n + sn + upsidedown[n] for sn in self._findStrobogrammatic(n - 2) for n in upsidedown]
            
    def _findStrobogrammatic(self, n):
        if n == 1:
            return ['0', '1', '8']
        elif n == 2:
            return ["00", "11","69","88","96"]
        else:
            upsidedown = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
            return [n + sn + upsidedown[n] for sn in self._findStrobogrammatic(n - 2) for n in upsidedown]
            
if __name__ == "__main__":
    n = 3
    print(Solution().findStrobogrammatic(n))
