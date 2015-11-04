package jg2;

public class Solution {
    public int jump(int[] nums) {
        int n = nums.length;
        int i = 0;
        int countJump = 0;
        
        while (i < n - 1) {
        	if (i + nums[i] >= n - 1) {
        		return countJump + 1;
        	}
        	int stepNext = 0;
        	int step = 0;
        	int j = 1;
        	while(j <= nums[i]) {
        		if (nums[i + j] + j >= stepNext) {
        			stepNext = nums[i + j] + j;
        			step = j;
        		}
        		j++;
        	}
        	i += step;
    		countJump++;
        }
        return countJump;
    }
    
    public static void main(String [] args) {
    	int [] nums = {1, 2, 3};
    	System.out.println(new Solution().jump(nums));
    }
}
