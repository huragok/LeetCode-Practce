package btbss;

public class Solution {
public int maxProfit(int[] prices) {
        int n = prices.length;
        if (n < 2) return 0;
        int profit = 0;
        int daysToBuy = 0;
        
        for (int i = 1; i < n; i++) {
        	if (prices[i - 1] < prices[daysToBuy]) {
        		daysToBuy = i - 1;
        	}
        	
        	if (prices[i] - prices[daysToBuy] > profit) {
        		profit = prices[i] - prices[daysToBuy];
        	}
        }
        return profit;
    }
}
