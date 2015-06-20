#!/usr/bin/env python

import sys
class Solution:
    # @param {integer} dividend
    # @param {integer} divisor
    # @return {integer}
    def divide(self, dividend, divisor):
        if divisor == 0:
            return sys.maxint
        elif divisor < 0:
            dividend = -dividend
            divisor = -divisor
        
        quotient = 0
        residual = dividend
        if dividend > 0:
            residual = dividend
        else:
            residual = -dividend
        while residual >= divisor:
            quotient_times_divisor = divisor
            quotient_part = 1
            while residual - quotient_times_divisor >= 0:
                quotient_times_divisor <<= 1
                quotient_part <<= 1
                
            residual -= (quotient_times_divisor >> 1)
            quotient += (quotient_part >> 1)
        
                
        if quotient >= 2 ** 31 or quotient < -(2 ** 31):
            quotient = 2 ** 31 - 1
            
        if dividend > 0:
            if quotient >= 2 ** 31:
                quotient = 2 ** 31 - 1
            return quotient
        else:
            if quotient > 2 ** 31:
                quotient = 1 - 2 ** 31
            return -quotient
        
if __name__ == "__main__":
    print(Solution().divide(-5, 2))
            
