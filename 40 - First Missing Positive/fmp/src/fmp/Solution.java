package fmp;

public class Solution {
    public int firstMissingPositive(int[] nums) {
        int n = nums.length;
        int tailPos = 0;
        int headZeroNeg = n;
        while (tailPos < headZeroNeg) {
        	if (nums[tailPos] == tailPos + 1) {
        		tailPos++;
        	}
        	else if (nums[tailPos] <= 0 || nums[tailPos] > n || nums[tailPos] == nums[nums[tailPos] - 1]) {
        		int tmp = nums[headZeroNeg - 1];
        		nums[headZeroNeg - 1] = nums[tailPos];
        		nums[tailPos] = tmp;
        		headZeroNeg--;
        	} else {
        		int tmp = nums[nums[tailPos] - 1];
        		nums[nums[tailPos] - 1] = nums[tailPos];
        		nums[tailPos] = tmp;
        	}
        }
        return headZeroNeg + 1;
    }
    
    public static void main(String [] args) {
    	int [] nums = {1, 1};
    	System.out.println(new Solution().firstMissingPositive(nums));
    }
}