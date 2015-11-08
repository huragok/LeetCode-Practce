package dw;

public class Solution {
	public int numDecodings(String s) {
        int n = s.length();
        if (n == 0 || s.charAt(0) == '0') {
        	return 0;
        } else if (n == 1) {
        	return 1;
        }
        
        int waysPrev = 0;
        int ways = 1;
        for (int i = 1; i < n; i++) {
        	int waysNew = 0;
        	if (s.charAt(i) != '0') {
        		waysNew += ways;
        	}
        	if (s.charAt(i - 1) != '0' && Character.getNumericValue(s.charAt(i)) + 10 * Character.getNumericValue(s.charAt(i - 1)) <= 26) {
        		waysNew += waysPrev;
        	}
        	waysPrev = ways;
        	ways = waysNew;
        }
        return ways;
    }
}
