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
            else:
                return nums[l]
        return min(nums[l], nums[r])
        
if __name__ == "__main__":
    nums = [2, 1]
    print(Solution().findMin(nums))
                
            
