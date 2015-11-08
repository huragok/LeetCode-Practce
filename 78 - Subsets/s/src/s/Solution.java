package s;

import java.util.Arrays;
import java.util.List;
import java.util.LinkedList;

public class Solution {
	public List<List<Integer>> subsets(int[] nums) {
		Arrays.sort(nums);
        List<Integer> candidates = new LinkedList<Integer> ();
        for (int i: nums) candidates.add(i);
        
        List<Integer> path = new LinkedList<Integer> ();
        List<List<Integer>> results = new LinkedList<List<Integer>> ();
        subsetsPartial(candidates, path, results);
        return results;
    }
	
	private void subsetsPartial(List<Integer> candidates, List<Integer> path, List<List<Integer>> results) {
		if (candidates.size() == 0) {
			results.add(new LinkedList<Integer> (path));
		} else {
			int c = candidates.get(0);
			candidates.remove(0);
			subsetsPartial(candidates, path, results);
			path.add(c);
			subsetsPartial(candidates, path, results);
			path.remove(path.size() - 1);
			candidates.add(0, c);
		}
		return;
	}
	
	public static void main(String [] args) {
		int [] nums = {1, 2, 3};
		System.out.println(new Solution().subsets(nums));
	}
}
