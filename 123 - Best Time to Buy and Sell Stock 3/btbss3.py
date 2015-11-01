class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        n = len(prices)
        if n < 2: # No transaction can be made
            return 0
        elif n == 2: # At most one transaction
            diff = prices[1] - prices[0]
            return diff if diff > 0 else 0
        elif n == 3: # Still at most one transaction, 4 cases
            return max([prices[2] - prices[1], prices[1] - prices[0], prices[2] - prices[0], 0])
            
        
        idx_left = 1
        idx_right = n - 2
        
        min_left = prices[0] # The minimum price to the left of or including day i
        max_right = prices[n - 1] # The maximum price to the right of or including day j
        
        benefit_left = [0] * (n + 1) # benefit_left[i] is the max benefit selling at or before day i - 1
        benefit_right = [0] * (n + 1) # benefit_right[j] is the max benefit by buying at or after day j
        for idx in range(1, n):
            if prices[idx_left] < min_left:
                min_left = prices[idx_left]
            benefit_left[idx_left + 1] = max([benefit_left[idx_left], prices[idx_left] - min_left])
            
            if prices[idx_right] > max_right:
                max_right = prices[idx_right]
            benefit_right[idx_right] =  max([benefit_right[idx_right+1], max_right - prices[idx_right]])
            
            idx_left += 1
            idx_right -= 1
         
        print(benefit_left)
        print(benefit_right)   
        max_benefit = 0
        for idx in range(n + 1):
            max_benefit = max([max_benefit, benefit_left[idx] + benefit_right[idx]])
            
        return max_benefit
        
if __name__ == "__main__":
    prices = [3,2,6,5,0,3]
    print(Solution().maxProfit(prices))
