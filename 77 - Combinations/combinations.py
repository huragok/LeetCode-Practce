class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {integer[][]}
    def combine(self, n, k):
        return self._combine(range(1, n+1), k)
        
    def _combine(self, nums, k):
    # @param {integer[]} nums (sorted)
    # @param {integer} k
    # @return {integer[][]}
    # Return all combinations of k numbers from nums
        n = len(nums)
        if n < k:
            return []
        elif k == 1:
            return [[n] for n in nums]
        else:
            comb = []
            for idx in range(n - k + 1):
                comb_rest = self._combine(nums[idx + 1 :], k - 1)
                for c in comb_rest:
                    comb.append([nums[idx]] + c)
            return comb
    
if __name__ == "__main__":
    n = 4
    k = 2
    print(Solution().combine(n, k))
    
    #print(Solution()._combine([3, 4], 1))
