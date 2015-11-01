class Solution:
    # @param nums, an integer[]
    # @return an integer
    def findPeakElement(self, nums):
        n = len(nums)
        if n == 1:
            return 0
            
        l = 0
        r = n - 1
        while r - l > 1:
            m = (l + r) / 2
            if nums[m] > nums[m - 1] and nums[m] > nums[m + 1]:
                return m
            elif nums[m] < nums[m - 1]:
                r = m - 1
            else:
                l = m + 1
        if nums[l] >= nums[r]:
            return l
        else:
            return r       
        
        
if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(Solution().findPeakElement(nums))
