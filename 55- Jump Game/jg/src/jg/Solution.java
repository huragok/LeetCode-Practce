package jg;

public class Solution {
	public boolean canJump(int[] nums) {
		int n = nums.length;
        
		int i = 0;
		while (i < n - 1) {
			if (nums[i] + i >= n - 1) {
				return true;
			}
			
			int stepNext = 0;
			int maxStep = 0;
			for (int step = 1; step <= nums[i]; step++) {
				if (step + nums[i + step] >= maxStep) {
					maxStep = step + nums[i + step];
					stepNext = step;
				}
			}
			if (stepNext == 0) {
				return false;
			} else {
				i += stepNext;
			}
		}
		return true;
    }
	
	public static void main(String [] args) {
		int [] nums = {3,2,1,0,4};
		System.out.println(new Solution().canJump(nums));
	}
}
