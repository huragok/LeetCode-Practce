class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        if n == 1:
            return 1
            
        count = 2
        n_ways = 2
        n_ways_prev = 1
        while count < n:
            (n_ways, n_ways_prev) = (n_ways + n_ways_prev, n_ways)
            count += 1
            
        return n_ways
