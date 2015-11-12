package pp;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	private int n;
	private String s;
	public List<List<String>> partition(String s) {
        n = s.length();
        this.s = s;
        List<List<String>> result = new ArrayList<List<String>> ();
        if (n > 0) {
        	List<String> path = new ArrayList<String> (n);
        	partition(0, path, result);
        }
        return result;
	}
	
	private void partition(int i, List<String> path, List<List<String>> result) {
		if (i == n) {
			result.add(new ArrayList<String> (path));
		}
		for (int j = i + 1; j <= n; j++) {
			if (isPalindrome(i, j)) {
				path.add(new String(s.substring(i, j)));
				partition(j, path, result);
				path.remove(path.size() - 1);
			}
		}
		return;
	}
	
	private boolean isPalindrome(int i, int j){
		for (int d = 0; d < (j - i) / 2; d++) {
			if (s.charAt(i + d) != s.charAt(j - 1 - d)) {
				return false;
			}
		}
		return true;
	}
}
