class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        n = len(prices)
        if n == 0:
            return 0
            
        benefit = 0
        for day in range(n - 1):
            benefit += max([prices[day + 1] - prices[day], 0])
            
        return benefit
