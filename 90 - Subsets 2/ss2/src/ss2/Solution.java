package ss2;

import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

public class Solution {
	public List<List<Integer>> subsetsWithDup(int[] nums) {
        Arrays.sort(nums);
        List<Integer> path = new ArrayList<Integer> (nums.length);
        List<List<Integer>> result = new ArrayList<List<Integer>> ();
        subsetsWithDupSince(nums, 0, path, result);
        return result;
    }
	
	private void subsetsWithDupSince(int [] nums, int idx, List<Integer> path, List<List<Integer>> result)
	{
		if (idx <= nums.length) {
			result.add(new ArrayList<Integer> (path));
		}
		
		while (idx < nums.length) {
			path.add(nums[idx]);
			subsetsWithDupSince(nums, idx + 1, path, result);
			path.remove(path.size() - 1);
			idx++;
			while (idx < nums.length && nums[idx] == nums[idx - 1]) idx++;
		}
		return;
	}
}
