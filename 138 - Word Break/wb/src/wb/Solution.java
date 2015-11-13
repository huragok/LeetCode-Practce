package wb;

import java.util.Set;

public class Solution {
	public boolean wordBreak(String s, Set<String> wordDict) {
		int n = s.length();
		boolean [] breakable = new boolean [n + 1]; // breakable[i] indicates whether s[0 :i] is breakable
		breakable[0] = true;
		
		// Start the DP;
		for (int i = 1; i <= n; i++) {
			breakable[i] = false;
			for (int l = 1; l <= i; l++) {
				if (wordDict.contains(s.substring(i - l, i)) && breakable[i - l]) {
					breakable[i] = true;
					break;
				}
			}
		}
		
		return breakable[n];
    }
}
