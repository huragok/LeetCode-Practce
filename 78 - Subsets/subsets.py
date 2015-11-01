class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsets(self, nums):
        return self._subsets(sorted(nums))
    
    def _subsets(self, nums):
        n = len(nums)
        if n == 0:
            return([[]])
        else:
            ss = []
            subsets_rest = self._subsets(nums[1 : ])
            for ssr in subsets_rest:
                ss.append([nums[0]] + ssr)
                ss.append(ssr)
            
            return ss
            
if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))
