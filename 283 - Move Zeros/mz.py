class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        
        if n == 0:
            return
            
        ptr_zero = -1
        ptr_nonzero = -1
        
        idx = 0
        ptr_nonzero = 0
        for idx in xrange(n):
            if nums[idx] == 0: # Find the first non zero to the right of idx
                ptr_nonzero = max([ptr_nonzero, idx])
                while ptr_nonzero < n and nums[ptr_nonzero] == 0:
                    ptr_nonzero += 1
                if ptr_nonzero == n:
                    return
                    
                nums[idx], nums[ptr_nonzero] = nums[ptr_nonzero], nums[idx] # swap
                
if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    Solution().moveZeroes(nums)
    print(nums)
                
