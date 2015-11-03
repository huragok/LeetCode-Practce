package sip;

public class Solution {
    public int searchInsert(int[] nums, int target) {
        int n = nums.length;
        if (target <= nums[0]) {
        	return 0;
        }
        if (target > nums[n - 1]) {
        	return n;
        }
        
        int left = 0, right = n - 1;
        while (right - left > 1) {
        	int mid = (left + right) / 2;
        	if (nums[mid] < target) {
        		left = mid;
        	} else {
        		right = mid;
        	}
        }
        return right;
    }
    
    public static void main(String [] args) {
    	int [] nums = new int [] {1, 3, 5, 6};
    	int target = 2;
    	System.out.println(new Solution().searchInsert(nums, target));
    }
}
