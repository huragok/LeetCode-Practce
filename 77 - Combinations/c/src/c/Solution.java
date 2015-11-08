package c;

import java.util.List;
import java.util.LinkedList;


public class Solution {
	public List<List<Integer>> combine(int n, int k) {
		List<Integer> candidates = new LinkedList<Integer> ();
		for (int i = 0; i < n; i++) {
			candidates.add(i + 1);
		}
		List<Integer> path = new LinkedList<Integer> ();
		List<List<Integer>> results = new LinkedList<List<Integer>> ();
		combinePartial(candidates, path, k, results);
		return results;
    }
	
	private void combinePartial(List<Integer> candidates, List<Integer> path, int k, List<List<Integer>> results) {
		if (candidates.size() < k) {
			return;
		} else if (k == 0) {
			results.add(new LinkedList<Integer> (path));
		} else {
			int c = candidates.get(candidates.size() - 1);
			candidates.remove(candidates.size() - 1);
			combinePartial(candidates, path, k, results);
			path.add(0, c);
			combinePartial(candidates, path, k - 1, results);
			path.remove(0);
			candidates.add(c);
		}
	}
	
	public static void main(String [] args) {
		int n = 4, k = 2;
		System.out.println(new Solution().combine(n, k));
	}
}
