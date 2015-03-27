#!/usr/bin/env python

class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows == 0:
            return s
        elif s == '':
            return ''
        elif nRows == 1:
            return s

        period = 2 * nRows - 2
        len_s = len(s)

        s_zigzag = [''] * nRows
        for iRows in range(nRows):
            if iRows == 0:
                s_zigzag[iRows] = s[0::period]
            elif iRows == nRows - 1:
                s_zigzag[iRows] = s[nRows-1::period]
            else:
                offset = nRows - iRows
                
                for left in range(iRows, len_s, period):
                    s_zigzag[iRows] += s[left]
                    if left + offset < len_s:
                        s_zigzag[iRows] += s[left + offset]
        return ''.join(s_zigzag)

if __name__ == "__main__":
    s = "abcdefghijk"
    #s = "A"
    nRows = 1

    print("s = {0}".format(s))
    print("zigzag = {0}".format(Solution().convert(s, nRows)))
