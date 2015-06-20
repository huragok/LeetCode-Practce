#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def nextPermutation(self, nums):
        n = len(nums) # Length of the list
        if n == 0 or n == 1:
            return
        # Starting from this position onward, the numbers are in Decreasing order
        idx = n - 1
        while idx >= 1 and nums[idx - 1] >= nums[idx]:
            idx -= 1
              
        if idx == 0: # The numbers are in the highest lexicalgraphical order, return the lowest possible value by reversing the order using swaping
            for i in range(n / 2):
                (nums[i], nums[n - i - 1]) = (nums[n - i - 1], nums[i])
        else: # use binary index to swap nums[idx - 1] with the smallest value in nums[idx : n] that is greater than nums[idx - 1] here we do not use bisect package
        
            left = idx
            right = n - 1
            val = nums[idx - 1]
            if nums[right] > val:
                (nums[idx - 1], nums[right]) = (nums[right], nums[idx - 1])
            else:
                while right - left > 1:
                    mid = (left + right) / 2
                    if nums[mid] > val:
                        left = mid
                    else:
                        right = mid

                (nums[idx - 1], nums[left]) = (nums[left], nums[idx - 1])
            
            # Sort the tail section in increasing order by reversing the order using swaping
            l = n - idx # Length of the sorted tail
            for i in range(l / 2):
                (nums[idx + i], nums[n - i - 1]) = (nums[n - i - 1], nums[idx + i])
                
            return
            
if __name__ == "__main__":
    nums = [3,6,8,8,8]
    Solution().nextPermutation(nums)
    print(nums)
    
        
            
