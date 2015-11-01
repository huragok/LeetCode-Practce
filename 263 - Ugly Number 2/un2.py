class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        
        ugly = [1] * n
        i2 = 0
        i3 = 0
        i5 = 0
        for idx in xrange(1, n):
            u2, u3, u5 = 2 * ugly[i2], 3 * ugly[i3], 5 * ugly[i5]
            umin = min(u2, u3, u5)
            ugly[idx] = umin
            if u2 == umin:
                i2 += 1
            if u3 == umin:
                i3 += 1
            if u5 == umin:
                i5 += 1
               
        return ugly[-1]
        
if __name__ == "__main__":
    n = 10
    print(Solution().nthUglyNumber(n))
