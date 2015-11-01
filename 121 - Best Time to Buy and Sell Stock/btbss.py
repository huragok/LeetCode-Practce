class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2:
            return 0
            
        min_height_left = prices[0] # The lowest price to the left, now ptr is at prices[1]
        max_benefit = prices[1] - prices[0]
        if max_benefit < 0:
            max_benefit = 0
        for idx in range(2, n):
            if prices[idx - 1] < min_height_left:
                min_height_left = prices[idx - 1]
            if prices[idx] - min_height_left > max_benefit:
                max_benefit = prices[idx] - min_height_left
                
        return max_benefit
