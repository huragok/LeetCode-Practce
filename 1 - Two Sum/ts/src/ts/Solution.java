package ts;

import java.util.*;

public class Solution {
	public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
        	map.put(nums[i], i);
        }
        
        for (int i = 0; i < nums.length; i++) {
        	if (map.containsKey(target - nums[i])) {
        		int idx2 = map.get(target - nums[i]);
        		if (idx2 > i)
        			return new int[] {i + 1, idx2 + 1};
        	}
        }
        return new int[] {0, 0};
    }
	 
	
	static public void main(String [] args) {
		int [] nums = new int [] {3, 2, 4};
		int target = 6;
		Solution sol = new Solution();
		System.out.println(Arrays.toString(sol.twoSum(nums, target)));
	}
}
