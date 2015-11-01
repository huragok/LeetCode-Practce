import collections
class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def subsetsWithDup(self, nums):
        hist = collections.defaultdict(int)
        for n in nums:
            hist[n] += 1
            
        keys, vals = zip(*sorted(list(hist.items()), key=lambda x: x[0]))
        return self._subsetWithDup(keys, vals)
        
    def _subsetWithDup(self, keys, vals):
        n = len(keys)
        if n == 0:
            return [[]]
        else:
            subsets_rest = self._subsetWithDup(keys[1:], vals[1:])
            num = keys[0]
            count = vals[0]
            return [[num] * n + subset for n in range(count + 1) for subset in subsets_rest]
            
if __name__ == "__main__":
    nums = [9, 3, 3]
    print(Solution().subsetsWithDup(nums))
                
