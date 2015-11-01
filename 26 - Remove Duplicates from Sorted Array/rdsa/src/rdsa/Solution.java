package rdsa;

import java.util.Arrays;

public class Solution {
	public int removeDuplicates(int[] nums) {
        if (nums.length == 0) {
        	return 0;
        } else if (nums.length == 1) {
        	return 1;
        } else {
        	int count = 1;
        	int tailUnique = 0;
        	int prob = 1;
        	while (prob < nums.length) {
        		if (nums[prob] != nums[tailUnique]) {
        			tailUnique++;
        			nums[tailUnique] = nums[prob];
        			count++;
        		}
        		prob++;
        	}
        	
        	return count;
        }
    }
	
	public static void main(String [] args) {
		int [] nums = {1, 1, 2};
		System.out.println(new Solution().removeDuplicates(nums));
		System.out.println(Arrays.toString(nums));
	}
}
