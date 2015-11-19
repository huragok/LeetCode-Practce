package escn;

public class Solution {
	public int titleToNumber(String s) {
		int n = s.length();
		int result = 0;
		for (int i = 0; i < n; i++) {
			int idx = s.charAt(i) - 'A' + 1;
			result = result * 26 + idx;
		}
		return result;
    }
}
