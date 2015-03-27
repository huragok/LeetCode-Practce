#!/usr/bin/env python3
class Solution:
    # @return an integer
    def reverse(self, x):
        x_str = str(abs(x)).rstrip('0')
        if x_str == '':
            return 0
        x_rev = int(x_str[::-1])
        if x < 0:
            x_rev *= -1
        elif x_rev > 2 ** 31 - 1 or x_rev < - 2 ** 31:
            return 0
        return x_rev

if __name__ == "__main__":
    x = 1234560000
    print(Solution().reverse(x))
