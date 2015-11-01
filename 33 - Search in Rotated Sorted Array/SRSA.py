#!/usr/bin/env python

class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        n = len(nums)
        if n == 0:
            return -1
            
        left = 0
        right = n - 1
        
        while right - left > 1 and nums[left] > nums[right]:
            mid = (left + right) / 2
            if nums[mid] > nums[left]:
                if nums[mid] >= target >= nums[left]:
                    right = mid
                else:
                    left = mid
            else: # nums[mid] < nums[right]
                if nums[mid] <= target <= nums[right]:
                    left = mid
                else:
                    right = mid
                    
        while right - left > 1: # nums[left] <= nums[right], we can do a normal bisect search
            if target < nums[left] or target > nums[right]:
                return -1
            mid = (left + right) / 2
            if target < nums[mid]:
                right = mid
            else:
                left = mid
                
        
        if nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        else:
            return -1
            
if __name__ == "__main__":
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    idx = Solution().search(nums, target)
    print(idx)
