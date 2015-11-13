package pp2;

import java.util.Arrays;

public class Solution {
	public int minCut(String s) {
		int n = s.length();
		int [] countCut = new int [n + 1]; // The minCut required for s[0 : i]
		countCut[0] = -1;
		for (int i = 1; i <= n; i++) {
			countCut[i] = i - 1;
		}

		for (int i = 0; i < n; i++) {

			// Test the palindrome centered at i (i - d : i + d + 1)
			int d;
			for (d = 0; d <= i && d < n - i; d++) {
				if (s.charAt(i - d) == s.charAt(i + d)) {
					if (countCut[i - d] + 1 < countCut[i + d + 1]) countCut[i + d + 1] = countCut[i - d] + 1;
				} else {
					break;
				}
			}
			
			
			// Test the palindrome with its left center at i (i - d : i + d + 2)
			if (i < n - 1 && s.charAt(i) == s.charAt(i + 1)) {
				for (d = 0; d <= i && d < n - i - 1; d++) {
					if (s.charAt(i - d) == s.charAt(i + 1 + d)) {
						if (countCut[i - d] + 1 < countCut[i + d + 2]) countCut[i + d + 2] = countCut[i - d] + 1;
					} else {
						break;
					}
				}
			}
		}
		return countCut[n];
    }
	
	public static void main(String [] args) {
		String s = "ccaacabacb";
		System.out.println(new Solution().minCut(s));
	}
}
