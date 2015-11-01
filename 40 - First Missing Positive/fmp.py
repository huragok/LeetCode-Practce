class Solution:
    # @param {integer[]} nums
    # @return {integer}
    
    def firstMissingPositive(self, nums):
        l = len(nums) # The length of the part that haven't be decided whether is missing or not
        i = 0 # The length of the part that has been sorted to be non-missing
        
        while i < l:
            if nums[i] == i + 1: # in right place
                i += 1 # scan the next
            elif nums[i] <= 0 or nums[i] > l or nums[i] == nums[nums[i] - 1]: # this value cannot be in the sorted part or is duplicated
                l -= 1 # move it to the end
                (nums[i], nums[l]) = (nums[l], nums[i])
            else: # 
                n = nums[i]
                (nums[i], nums[n - 1]) = (nums[n - 1], nums[i]) # swap it to the right place
             
        return l + 1
        
if __name__ == "__main__":
    nums = [2,1]
    x = Solution().firstMissingPositive(nums)
    print(x)
