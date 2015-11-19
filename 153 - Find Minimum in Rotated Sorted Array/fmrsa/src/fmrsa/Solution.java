package fmrsa;

public class Solution {
	public int findMin(int[] nums) {
		int n = nums.length;
		if (n == 1) return nums[0];
		
		int left = 0, right = n - 1;
		
		while (right - left > 1 && nums[left] > nums[right]) {
			int mid = (left + right) / 2;
			if (nums[mid] > nums[left]) {
				left = mid;
			} else {
				right = mid;
			}
		}
		
		if (right - left == 1) {
			return nums[left] > nums[right] ? nums[right] : nums[left];
		} else {
			return nums[left];
		}
        
    }
}
