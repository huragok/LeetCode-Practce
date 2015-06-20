#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def removeDuplicates(self, nums):
        n_num = len(nums)
        if n_num == 0:
            return 0
            
        
        val_current = nums[0]
        i_num = 0
        while i_num < n_num:
            i_rep = i_num + 1
            while i_rep < n_num and nums[i_rep] == val_current:
                i_rep += 1
              
            if i_rep < n_num:
                val_current = nums[i_rep]
                
            nums[i_num + 1 : i_rep] = []
            n_num -= (i_rep - i_num - 1)
            i_num += 1
                
        return n_num
        
if __name__ == "__main__":
    nums = list(map(int, [1,1,2]))
    n_num = len(nums)

    val_current = nums[0]
    i_num = 0
    while i_num < n_num:
        i_rep = i_num + 1
        print(val_current)
        print("i_rep = {0}".format(i_rep))
        while i_rep < n_num and nums[i_rep] == val_current:
            i_rep += 1
            print("i_rep = {0}".format(i_rep))
            
        if i_rep < n_num:
            val_current = nums[i_rep]
        
        print("time to remove")
        print(i_num)
        print(i_rep)
        nums[i_num + 1 : i_rep] = []
        n_num -= (i_rep - i_num - 1)
        i_num += 1
        
                
