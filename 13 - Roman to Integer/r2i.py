#!/usr/bin/env python

class Solution:
    # @return an integer
    def romanToInt(self, s):
        mapping = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        subtract_from = {'C':('M', 'D'), 'X':('C','L'), 'I':('X', 'V')}
        

        integer = 0
        for idx in range(len(s)):
            if idx == 0:
                integer += mapping[s[idx]]
            elif s[idx-1] in subtract_from.keys() and s[idx] in subtract_from[s[idx-1]]:
                integer += mapping[s[idx]] - 2 * mapping[s[idx-1]]
            else:
                integer += mapping[s[idx]]
                
        return integer
        
if __name__ == "__main__":
    sol = Solution()
    romans = ('MCMLIV', 'MCMXC', 'MMXIV')
    for s in romans:
        print("{0}: {1}".format(s, sol.romanToInt(s)))
        
