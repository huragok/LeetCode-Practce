package mr;

import java.util.List;
import java.util.ArrayList;
public class Solution {
	public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        int boundLeft = lower; // Left bound of the missing interval included
        int boundRight = lower; // Right bound of the missing interval not included
        List<String> result = new ArrayList<String> ();
        
        for (int num: nums) {
        	if (num == boundLeft) {
        		boundLeft++;
        		boundRight = boundLeft;
        	} else {
        		boundRight = num;
        		if (boundRight - 1 == boundLeft) {
        			result.add(Integer.toString(boundLeft));
        		} else {
        			result.add(Integer.toString(boundLeft) + "->" + Integer.toString(boundRight - 1));
        		}
        		boundLeft = num + 1;
        		boundRight = boundLeft;
        	}
        }
        if (boundLeft <= upper) {
        	if (upper == boundLeft) {
        		result.add(Integer.toString(upper));
        	} else {
        		result.add(Integer.toString(boundLeft) + "->" + Integer.toString(upper));
        	}
        }
        return result;
    }
	
	public static void main(String [] args) {
		int [] nums = {0, 1, 3, 50, 75};
		int lower = 0, upper = 99;
		System.out.println(new Solution().findMissingRanges(nums, lower, upper));
	}
}
