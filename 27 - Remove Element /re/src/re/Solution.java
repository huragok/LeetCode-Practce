package re;

import java.util.Arrays;

public class Solution {
	public int removeElement(int[] nums, int val) {
        int tailRemoved = -1;
        int probe = 0;
        int len = nums.length;
        
        while (probe < nums.length) {
        	if (nums[probe] != val) {
        		tailRemoved++;
        		nums[tailRemoved] = nums[probe];
        	} else {
        		len--;
        	}
        	probe++;
        }
        return len;
    }
	
	public static void main(String [] args) {
		int [] nums = {1, 2, 3, 2, 1, 2};
		int val = 2;
		System.out.println(new Solution().removeElement(nums, val));
		System.out.println(Arrays.toString(nums));
	}
}
