#!/usr/bin/env python

class Solution:
    # @return a string
    def intToRoman(self, num):
        s_num = str(num)
        digits = ['0'] * 4
        for i in range(1, len(s_num) + 1):
            digits[-i] = s_num[-i]
            
        # Starting from the left most digits
        dict_1000 = {'0': '', '1': 'M', '2': 'MM', '3':'MMM'}
        dict_100 = {'9':'CM', '8':'DCCC', '7':'DCC', '6':'DC', '5':'D', '4':'CD', '3':'CCC', '2':'CC', '1':'C', '0':''}
        dict_10 = {'9':'XC', '8':'LXXX', '7':'LXX', '6':'LX', '5':'L', '4':'XL', '3':'XXX', '2':'XX', '1':'X', '0':''}
        dict_1 = {'9':'IX', '8':'VIII', '7':'VII', '6':'VI', '5':'V', '4':'IV', '3':'III', '2':'II', '1':'I', '0':''}
        
        roman = dict_1000[digits[0]] + dict_100[digits[1]] + dict_10[digits[2]] + dict_1[digits[3]]
        
        return roman
        
if __name__ == "__main__":
    nums = (1954, 1990, 2014)
    sol = Solution()
    for num in nums:
        print("{0}: {1}".format(num, sol.intToRoman(num)))
