class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        n = len(nums)
        if n == 0:
            return 0
        elif n == 1:
            return nums[0]
        elif n == 2:
            return max(nums)    
            
        max_with0 = nums[0]
        max_prev_with0 = nums[0]
        
        max_without0 = nums[1]
        max_prev_without0 = 0
        
        for idx in range(2, n):
            (max_without0, max_prev_without0) = (max([max_without0, max_prev_without0 + nums[idx]]), max_without0)
            
        for idx in range(2, n - 1):
            (max_with0, max_prev_with0) = (max([max_with0, max_prev_with0 + nums[idx]]), max_with0)
            
        return max([max_with0, max_without0])
        
        
            
            
