

class Solution:
    # @param {integer[]} nums
    # @return {integer[][]}
    def permuteUnique(self, nums):
        from collections import Counter
        nums_dict = Counter(nums)
        (nums, counts) = (nums_dict.keys(), nums_dict.values())
        return self._permuteUnique(nums, counts, len(nums), sum(counts))
        
    def _permuteUnique(self, nums, counts, n, sum_count):
        # @param {integer[]} nums
        # @param {integer[]} counts
        # @param {integer[]} n
        # @param {integer[]} sum_count
        # @return {integer[][]}
        if len(nums) == 1:
            return [nums * counts[0]]
        else:
            num = nums[0]
            count = counts[0]
            poss_num = self._combination(count, 0, sum_count)
            permutations_sub = self._permuteUnique(nums[1:], counts[1:], n-1, sum_count-count)
            
            permutation = [self._insert(pos, permutation_sub, num) for pos in poss_num for permutation_sub in permutations_sub]
     
            return permutation
            
    # Function to select k position among [n_start : n_end]        
    def _combination(self, k, n_start, n_end):
        if k == 1:
            return map(list, zip(range(n_start, n_end)))
        elif k == n_end - n_start:
            return [range(n_start, n_end)]
        else:   
            combination = [[pos] + combination_sub for pos in range(n_start, n_end - k + 1) for combination_sub in self._combination(k - 1, pos + 1, n_end)]
            return combination
            
    def _insert(self, pos, fill, d):
        r = []
        s = -1
        p_fill = 0
        for p in pos:
            r += fill[p_fill: p_fill + p - s - 1] + [d]
            p_fill += p - s - 1
            s = p
        r += fill[p_fill :]
        return r
 
if __name__ == "__main__":
    #n = 5
    #k = 3
    #print(Solution()._combination(k, 0, n))

    #fill = ['a', 'b', 'c', 'd', 'e']
    #d = 'x'
    #pos = [5,6,7]
    #print(Solution()._insert(pos, fill, d))
    
    nums = [1, 1]
    print(Solution().permuteUnique(nums))
