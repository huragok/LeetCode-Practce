package p2;

import java.util.List;
import java.util.LinkedList;
import java.util.Set;
import java.util.HashSet;
import java.util.Arrays;

public class Solution {
    public List<List<Integer>> permuteUnique(int[] nums) {
        Arrays.sort(nums);
        List<Integer> path = new LinkedList<Integer> ();
        Set<Integer> rest = new HashSet<Integer> (nums.length);
        for (int i = 0; i < nums.length; i++) {
        	rest.add(i);
        }
        List<List<Integer>> result = new LinkedList<List<Integer>> ();
        permuteUniquePartial(path, rest, nums, result);
        return result;
    }
    
    private void permuteUniquePartial(List<Integer> path, Set<Integer> rest, int[] nums, List<List<Integer>> result) {
    	if (path.size() == nums.length) { // A full path
    		List<Integer> entry = new LinkedList<Integer> ();
    		for (int i= 0; i < nums.length; i++) {
    			entry.add(nums[path.get(i)]);
    		}
    		result.add(entry);
    	} else {
    		Set<Integer> restSnapShot = new HashSet<Integer>(rest);
    		Set<Integer> valVisited = new HashSet<Integer>();
    		for (int pos: restSnapShot) {
    			if (!valVisited.contains(nums[pos])) {
    				path.add(pos);
        			rest.remove(pos);
        			permuteUniquePartial(path, rest, nums, result);
        			rest.add(pos);
        			path.remove(path.size() - 1);
        			valVisited.add(nums[pos]);
    			}
    		}
    	}
    }
    
    public static void main(String [] args) {
    	int [] nums = {1, 2, 1};
    	System.out.println(new Solution().permuteUnique(nums));
    }
}
