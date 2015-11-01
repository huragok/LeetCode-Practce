package s3;

import java.util.*;

public class Solution {
	public List<List<Integer>> threeSum(int[] nums) {
		Arrays.sort(nums);
		//System.out.println(Arrays.toString(nums));
        
        List<List<Integer>> result = new ArrayList<List<Integer>>();
        int i = 0;
        while (i < nums.length - 2) {
        	
        	if (nums[i] > 0) {
        		break;
        	}
        	int j = i + 1;
        	int k = nums.length - 1;
        	
        	while (k > j) {
        		if (nums[j] + nums[k] == -nums[i]) {

    				List<Integer> tmp = new ArrayList<Integer>(3);
            		tmp.add(nums[i]); tmp.add(nums[j]); tmp.add(nums[k]);
            		result.add(tmp);

            		k--; j++;
            		while (k > j && nums[k] == nums[k + 1]) k--;
            		while (j < k && nums[j] == nums[j - 1]) j++;
        		} else if (nums[j] + nums[k] > -nums[i]) {
        			k--;
        			while (k > j && nums[k] == nums[k + 1]) k--;
        		} else {
        			j++;
        			while (j < k && nums[j] == nums[j - 1]) j++;
        		}
        	}
        	
        	while (i + 1 < nums.length && nums[i + 1] == nums[i]) i++;
        	i++;
        }
        return result;
    }
	
	public static void main(String [] args) {
		int [] nums = {0,0,0,0}; 
		System.out.println(new Solution().threeSum(nums));
	}
}
