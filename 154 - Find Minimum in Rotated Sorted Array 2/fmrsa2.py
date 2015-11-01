class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def findMin(self, nums):
        
        n = len(nums)
        l = 0
        r = n - 1
        while r > l + 1:
            m = (l + r) / 2
            if nums[m] > nums[r]:
                l = m
            elif nums[m] < nums[l]:
                r = m
            elif nums[l] < nums[m] < nums[r]:
                return nums[l]
            else:
                r -= 1
                
        return min(nums[l], nums[r])
