package fpe;

public class Solution {
	public int findPeakElement(int[] nums) {
		int n = nums.length;
		if (n == 0) return -1;
		if (n == 1) return 0;
		
		int left = 0, right = n - 1; // nums[left] must be greater than nums[left - 1], nums[right] > nums[right + 1]
		while (right - left > 1) {
			int mid = (left + right) / 2;
			if (nums[mid] > nums[mid - 1] && nums[mid] > nums[mid + 1]) {
				return mid;
			} else if (nums[mid] < nums[mid - 1]) {
				right = mid - 1;
			} else {
				left = mid + 1;
			}
		}
		return nums[left] > nums[right] ? left : right;
    }
}
