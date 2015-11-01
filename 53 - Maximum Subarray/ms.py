class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        n = len(nums)

        max_sub_end = [0] * n
        max_sub_end[0] = nums[0]  # max_sub_end is the maximum sum of an array ends in nums[i]         
        for i in range(1, n):
            num = nums[i]
            
            if max_sub_end[i - 1] < 0:
                max_sub_end[i] = num
            else:
                max_sub_end[i] = max_sub_end[i - 1] + num
        return max(max_sub_end)
        
if __name__ == "__main__":
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(Solution().maxSubArray(nums))
                
    
