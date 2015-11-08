package srsa2;

public class Solution {
	public boolean search(int[] nums, int target) {
        int n = nums.length;
        if (n == 0) return false;
        int left = 0, right = n - 1;
        if (nums[left] == target) return true;
        
        while (left < right && nums[left] == nums[right]) {
        	left++;
        }
        if (left == right) return false;
        
        while (right - left > 1 && nums[right] < nums[left]) {
        	int mid = (left + right) / 2;
        	if (nums[mid] >= nums[left]) {
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
        }
        
        if (nums[right] == target || nums[left] == target) {
        	return true;
        } else if (nums[left] > target || nums[right] < target) {
        	return false;
        }
        
        
        while (right - left > 1) {
        	int mid = (left + right) / 2;
        	if (nums[mid] == target) {
        		return true;
        	} else if (nums[mid] < target) {
        		left = mid;
        	} else {
        		right = mid;
        	}
        }
        return false;
    }
}
