class Solution(object):
    def wiggleSort(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        for idx in range(1, n):
            if (idx & 1 == 1) ^ (nums[idx] < nums[idx - 1]):
                nums[idx],  nums[idx - 1] = nums[idx - 1],  nums[idx]
                
        return
