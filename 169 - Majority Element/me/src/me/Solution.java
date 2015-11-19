package me;

public class Solution {
	public int majorityElement(int[] nums) {
        int n = nums.length;
		int major = nums[0];
        int count = 1;
        for (int i = 1; i < n; i++) {
        	if (nums[i] == major) {
        		count++;
        	} else {
        		count--;
        		if (count < 0) {
        			major = nums[i];
        			count = 1;
        		}
        	}
        }
        return major;
    }
}
