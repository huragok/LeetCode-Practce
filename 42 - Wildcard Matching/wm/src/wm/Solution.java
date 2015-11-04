package wm;

public class Solution {
    public boolean isMatch(String s, String p) {
    	int n = s.length();
        int m = p.length();
        

        boolean [] match = new boolean [n + 1]; // whether s[0:j] can be matched to p[0:i]
        match[0] = true; // Initialize: i = 0
        for (int i = 1; i <= m; i++) {
        	char c = p.charAt(i - 1);
        	
        	if (c == '?') {
        		for (int j = n; j >= 1; j--) {
        			match[j] = match[j - 1];
        		}
        	} else if (c != '*') {
        		for (int j = n; j >= 1; j--) {
    				match[j] = match[j - 1] & (s.charAt(j - 1) == c);
        		}		
        	} else {
        		for (int j = 1; j <= n; j++) {
        			match[j] |= match[j - 1]; 
        		}
        	}
        	match[0] &= (c == '*');
        }
        return match[n];
    }
    
    public static void main(String [] args) {
    	String s = "aa";
    	String p = "aaa";
    	System.out.println(new Solution().isMatch(s, p));
    }
}
