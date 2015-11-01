class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {boolean}
    def search(self, nums, target):
        n = len(nums)
        l = 0
        r = n - 1
        
        # When the breaking point is still inside the window
        while r > l:
            m = (l + r) / 2
            if nums[m] == target:
                return True
            if nums[m] > nums[r]:
                if target >= nums[l] and target < nums[m]:
                    r = m
                else:
                    l = m + 1
            elif nums[m] < nums[r]:
                if target > nums[m] and target <= nums[r]:
                    l = m + 1
                else:
                    r = m
            elif nums[l] != nums[r]:
                r = m
            else:
                r -= 1
            print(l, r)
        return True if nums[l] == target else False
        
if __name__ == "__main__":
    nums = [1, 3]
    target = 3
    print(Solution().search(nums, target))
