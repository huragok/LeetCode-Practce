class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        nd = len(str(n)) # Number of digits in n
        
        count = [0] * nd # count[n] is the number of digit 1 in 0 ~ 10 ** n - 1
        count[0] = 0
        for idx in range(1, nd):
            count[idx] = 10 * count[idx - 1] + 10 ** (idx - 1)
        print(count)
        count_total = 0
        for idx, d in enumerate(list(map(int, str(n)))):
            idx_bit = nd - idx - 1
            n -= d * 10 ** idx_bit
            if d != 0:
                print(idx_bit, d)
                count_total += d * count[idx_bit]
                if d == 1:
                    count_total += n + 1
                else:
                    count_total += 10 ** idx_bit
                print(count_total)    
        return count_total
        
if __name__ == "__main__":
    n = 21
    print(Solution().countDigitOne(n))
