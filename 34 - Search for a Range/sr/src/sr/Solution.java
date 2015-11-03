package sr;
import java.util.Arrays;
public class Solution {
    public int[] searchRange(int[] nums, int target) {
        int n = nums.length;
        if (target < nums[0] || target > nums[n - 1]) {
        	return new int [] {-1, -1};
        }
        
        int low = -1, high = -1;
        int left, right;
        
        // Search for the low end
        left = 0; right = n - 1;
        if (nums[left] == target) {
        	low = left;
        } else { // maintain nums[left] < target and nums[right] >= target
        	while (right - left > 1) {
        		int mid = (left + right) / 2;
        		if (nums[mid] >= target) {
        			right = mid;
        		} else {
        			left = mid;
        		}
        	}
        	if (nums[right] == target) {
        		low = right;
        	} else {
        		return new int [] {-1, -1};
        	}
        }
        
     // Search for the high end
        left = 0; right = n - 1;
        if (nums[right] == target) {
        	high = right;
        } else { // maintain nums[left] <= target and nums[right] > target
        	while (right - left > 1) {
        		int mid = (left + right) / 2;
        		if (nums[mid] > target) {
        			right = mid;
        		} else {
        			left = mid;
        		}
        	}
        	if (nums[left] == target) {
        		high = left;
        	} else {
        		return new int [] {-1, -1};
        	}
        }
        
        return new int [] {low, high};
    }
    
    public static void main (String [] args) {
    	int nums [] = {5, 7, 7, 8, 8, 10};
    	int target = 7;
    	System.out.println(Arrays.toString(new Solution().searchRange(nums, target)));
    }
}