class Solution(object):

    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        upsidedown = {0:0, 1: 1, 6: 9, 8: 8, 9: 6}
        num = list(map(int, str(num)))
        n = len(num)
        for idx in range(n - n / 2):
            if num[idx] not in upsidedown or upsidedown[num[idx]] != num[n - 1 - idx]:
                return False
                
        return True
        
if __name__ == "__main__":
    num = 69
    print(Solution().isStrobogrammatic(num))
            
            
