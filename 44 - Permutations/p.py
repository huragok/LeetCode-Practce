class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permute(self, nums):
        return self._permute(nums)
        
    def _permute(self, nums):
        n = len(nums)
        if n == 1:
            return [nums]
        else:
            num = nums[0]
            permutation_sub = self._permute(nums[1 :])
            permutation = [p[0 : pos] + [num] + p[pos :] for pos in range(n) for p in permutation_sub]
            return permutation
            
if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    x = Solution().permute(nums)
    print(x)
