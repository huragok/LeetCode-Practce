class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        nums_set = set(nums)
        len_max = 0
        for n in nums_set:
            if n - 1 not in nums_set:
                m = n + 1:
                while m in nums_set:
                    m += 1
                    
                if m - n > len_max:
                    len_max = m - n
                    
        return len_max
