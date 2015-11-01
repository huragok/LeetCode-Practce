class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer[]}
    def searchRange(self, nums, target):
        n = len(nums)
        left = 0
        right = n - 1
        
        if n < 1 or target > nums[right] or target < nums[left]:
            return [-1, -1]
            
        # Find the smallest index that is greater than the target (right bound)
        r = -1
        if nums[right] == target:
            r = right
        else:    
            while right - left > 1:
                mid = (left + right) / 2
                if nums[mid] > target:
                    right = mid # Right always > target
                else:
                    left = mid # Left always <= target
            if nums[left] == target:
                r = left
            else:
                return [-1, -1]
        
        # Find the largest index that is smaller than or equal to the target (left bound)
        left = 0
        
        l = -1
        if nums[left] == target:
            l = left
        else:    
            while right - left > 1:
                mid = (left + right) / 2
                if nums[mid] >= target:
                    right = mid # Right always >= target
                else:
                    left = mid # Left always < target
            l = right
        
        return [l, r]
        
if __name__ == "__main__":
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(Solution().searchRange(nums, target))
