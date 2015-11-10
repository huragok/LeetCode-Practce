package btbss3;

public class Solution {
	public int maxProfit(int[] prices) {
        int n = prices.length;
        if (n == 0) return 0;
        int [] maxProfitBefore = new int [n];
        maxProfitBefore[0] = 0;
        int dayBuy = 0;
        for (int i = 1; i < n; i++) {
        	if (prices[i - 1] < prices[dayBuy]) {
        		dayBuy = i - 1;
        	}
        	
        	if (maxProfitBefore[i - 1] < prices[i] - prices[dayBuy]) {
        		maxProfitBefore[i] = prices[i] - prices[dayBuy];
        	} else {
        		maxProfitBefore[i] = maxProfitBefore[i - 1];
        	}
        }
        
        int [] maxProfitAfter = new int [n];
        maxProfitAfter[n - 1] = 0;
        int daySell = n - 1;
        for (int i = n - 2; i >= 0; i--) {
        	if (prices[i + 1] > prices[daySell]) {
        		daySell = i + 1;
        	}
        	
        	if (maxProfitAfter[i + 1] < prices[daySell] - prices[i]) {
        		maxProfitAfter[i] = prices[daySell] - prices[i];
        	} else {
        		maxProfitAfter[i] = maxProfitAfter[i + 1];
        	}
        }
        
        int profit = 0;
        for (int i = 0; i < n; i++) {
        	int profitTmp = maxProfitBefore[i] + maxProfitAfter[i];
        	if (profit < profitTmp) profit = profitTmp;
        }
        return profit;
    }
}
