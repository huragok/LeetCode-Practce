class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def searchInsert(self, nums, target):
        # i.e. Find the index of the smallest value in nums that is greater than or equal to the target
        n = len(nums)
        if n < 1:
            return 0
            
        left = 0
        right = n - 1
        
        if nums[right] < target:
            return n
        if nums[left] >= target:
            return 0
            
        while right - left > 1:
            mid = (right + left) / 2
            if nums[mid] >= target:
                right = mid # Right always greater than or equal to target
            else:
                left = mid # Left always smaller than target
                
        print(left, right)
        return right
        
if __name__ == "__main__":
    nums = [1,3]
    target = 1
    print(Solution().searchInsert(nums, target))
            
