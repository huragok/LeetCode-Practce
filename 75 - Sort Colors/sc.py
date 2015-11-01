class Solution:
    # @param {integer[]} nums
    # @return {void} Do not return anything, modify nums in-place instead.
    def sortColors(self, nums):
        
        n = len(nums)
        # Float the zeros
        ptr_zero = -1
        
        for ptr_probe in range(n):
            if nums[ptr_probe] == 0:
                ptr_zero += 1
                (nums[ptr_probe], nums[ptr_zero]) = (nums[ptr_zero], nums[ptr_probe])
                
        # Float the ones
        ptr_one = ptr_zero
        for ptr_probe in range(ptr_zero + 1, n):
            if nums[ptr_probe] == 1:
                ptr_one += 1
                (nums[ptr_probe], nums[ptr_one]) = (nums[ptr_one], nums[ptr_probe])
        return
        
if __name__ == "__main__":
    nums = [0, 1, 2,2, 1, 0, 0,2]
    Solution().sortColors(nums)
    print(nums)
