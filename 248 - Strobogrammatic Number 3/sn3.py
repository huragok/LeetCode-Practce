class Solution(object):
    def strobogrammaticInRange(self, low, high):
        """
        :type low: str
        :type high: str
        :rtype: int
        """
        ll = len(low)
        lh = len(high)
        count = 0
        upsidedown = {'1': '1', '6': '9', '8': '8', '9': '6'}
        if int(low) > int(high):
            return 0
        elif ll == lh:
            return self._strobogrammaticInRange(ll, low, high, upsidedown)
        else:
            count += self._strobogrammaticInRange(ll, low, '9' * ll, upsidedown)
            count += self._strobogrammaticInRange(lh, '0' * lh, high, upsidedown)
            for d in range(ll + 1, lh):
                count += self._strobogrammaticInRange(d, '0' * d, '9' * d, upsidedown)
            return count
        
        
    def _strobogrammaticInRange(self, n, low, high, upsidedown):
        ll = len(low)
        lh = len(high)
        if lh < n or ll > n or ll > lh or int(low) > int(high):
            return 0
        if lh > n:
            high = '9' * n
        if ll < n:
            low = '0' * n
            
        if n == 1:
            return len([num for num in ['0', '1', '8'] if low <= num <= high])
        elif n == 2:
            if '0' in upsidedown:
                return len([num for num in ['00', '11', '69', '88', '96'] if low <= num <= high])
            else:
                return len([num for num in ['11', '69', '88', '96'] if low <= num <= high])
        else:
            upsidedown_new = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'} 
            count = 0
            count_sub_full = self._strobogrammaticInRange(n - 2, '0' * (n-2), '9' * (n-2), upsidedown_new)
            if low[0] < high[0]:
                for num in upsidedown:
                    if low[0] < num < high[0]:
                        count += count_sub_full
                    elif num == high[0]:
                        
                        if high[-1] >= upsidedown[num]:
                            count += self._strobogrammaticInRange(n - 2, '0' * (n - 2), high[1 : lh - 1], upsidedown_new)
                        elif high[1 : n - 1] > '0':
                            count += self._strobogrammaticInRange(n - 2, '0' * (n - 2), str(int(high[1 : n - 1]) - 1).zfill(n - 2), upsidedown_new)
                    elif num == low[0]:
                        if low[-1] <= upsidedown[num]:
                            count += self._strobogrammaticInRange(n - 2, low[1 : ll - 1], '9' * (n - 2), upsidedown_new)                    
                        elif low[1 : n - 1] < '9' * (n - 2):
                            count += self._strobogrammaticInRange(n - 2, str(int(low[1 : n - 1]) + 1).zfill(n - 2), '9' * (n - 2), upsidedown_new)
            elif low[0] == high[0]:
                for num in upsidedown:
                    if num == low[0]:
                        if low[-1] <= upsidedown[num]:
                            lowerbound = low[1 : ll - 1]
                        elif low[1] < '9':
                            lowerbound = str(int(low[1 : n - 1]) + 1).zfill(n - 2), '9' * (n - 2)
                        else:
                            lowerbound = '1' + '0' * (n - 2)
                            
                        if high[-1] >= upsidedown[num]:
                            upperbound = high[1 : lh - 1]
                        elif high[1] > '0':
                            upperbound = str(int(high[1 : n - 1]) - 1).zfill(n - 2)
                        else:
                            upperbound ='0' * (n - 3)
                            
                        count += self._strobogrammaticInRange(n - 2, lowerbound, upperbound, upsidedown_new)
                        
            return count
            
if __name__ == "__main__":
    low = '100'
    high = '1000'
    print(Solution().strobogrammaticInRange(low, high))
    
