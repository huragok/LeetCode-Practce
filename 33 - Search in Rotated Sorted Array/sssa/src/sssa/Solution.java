package sssa;

public class Solution {
    public int search(int[] nums, int target) {
        int n = nums.length;
        int left = 0;
        int right = n - 1;
        
        
        while (right - left > 1 && nums[left] > nums[right]) {
        	int mid = (left + right) / 2;
        	if (nums[mid] > nums[left]) {
        		if (target >= nums[left] && target <= nums[mid]) {
        			right = mid;
        		} else {
        			left = mid;
        		}
        	} else {
        		if (target >= nums[mid] && target <= nums[right]) {
        			left = mid;
        		} else {
        			right = mid;
        		}
        	}
        	System.out.println(left);
            System.out.println(right);
        }
        
        if (right - left == 1) {
        	if (nums[left] == target) {
            	return left;
            }
            if (nums[right] == target) {
            	return right;
            }
            return -1;
        }
        if (target < nums[left] || target > nums[right]) {
        	return -1;
        }
        
        
        while (right - left > 1) {
        	int mid = (left + right) / 2;
        	if (nums[mid] == target) {
        		return mid;
        	} else if (nums[mid] > target) {
        		right = mid;
        	} else {
        		left = mid;
        	}
        }
        if (nums[left] == target) {
        	return left;
        }
        if (nums[right] == target) {
        	return right;
        }
        return -1;
    }
    
    public static void main(String args []) {
    	int [] nums = {5, 1, 3};
    	int target = 3;
    	System.out.println(new Solution().search(nums, target));
    }
}