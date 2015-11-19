package hr;

public class Solution {
	public int rob(int[] nums) {
		int n = nums.length;
		if (n == 0) return 0;
        int sumPrev = 0;
        int sumCurr = nums[0];
        
        for (int i = 1; i < n; i++) {
        	int sumNew = sumPrev + nums[i];
        	if (sumNew < sumCurr) sumNew = sumCurr;
        	
        	sumPrev = sumCurr;
        	sumCurr = sumNew;
        }
        return sumCurr;
    }
}
