package oed;

public class Solution {
	public boolean isOneEditDistance(String s, String t) {
		int m = s.length(), n = t.length();
        
		if (m - n > 1 || m - n < -1) return false;
		
		if (m > n) { // make sure m <= n
			String tmp = s;
			s = t; 
			t = tmp;
			int x = m; m = n; n = x;
		}
		
		if (m == n) {
			int countDif = 0;
			for (int i = 0; i < n; i++) {
				if (s.charAt(i) != t.charAt(i)) countDif++;
				if (countDif >= 2) return false;
			}
			return countDif == 1;
		} else {
			int i;
			for (i = 0; i < m; i++) {
				if (s.charAt(i) != t.charAt(i)) break;
			}

			for (; i < m; i++) {
				if (s.charAt(i) != t.charAt(i + 1)) return false;
			}
			return true;
		}
    }
}
