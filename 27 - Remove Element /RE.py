#/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @param {integer} val
    # @return {integer}
    def removeElement(self, nums, val):
        n_num = len(nums)
        i_num = 0
        while i_num < n_num:
            if nums[i_num] == val:
                del nums[i_num]
                n_num -= 1
            else:
                i_num += 1
        return n_num
                
