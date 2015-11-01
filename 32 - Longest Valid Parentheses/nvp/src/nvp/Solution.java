package nvp;

public class Solution {
	public int longestValidParentheses(String s) {
		int n = s.length();
        int [] lengthTail = new int[n];
        
        int lenMax = 0;
        for (int i = 0; i < n; i++) {
        	char c = s.charAt(i);
        	if (c == '(') {
        		lengthTail[i] = 0;
        	} else if (i > 0) {
        		int left = i - 1;
        		int lenTmp = 0;
        		if (s.charAt(left) == '(') {
        			if (i >= 2) {
        				lengthTail[i] = lengthTail[i - 2] + 2;
        			} else {
        				lengthTail[i] = 2
        			}
        		} else {
        			if (left < lengthTail[left])
        		}
        	}
        }
    }
}
