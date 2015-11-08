package mws;

import java.util.Map;
import java.util.HashMap;

public class Solution {
	public String minWindow(String s, String t) {
		int m = t.length();
		int n = s.length();
		
		int numCovered = 0; // Number of chars covered by the current window
		Map<Character, Integer> charUncovered = new HashMap<Character, Integer> ();
		for (int i = 0; i < m; i++) {
			char c = t.charAt(i);
			if (charUncovered.containsKey(c)) {
				charUncovered.put(c, charUncovered.get(c) + 1);
			} else {
				charUncovered.put(c, 1);
			}
		}
		int lenMinWindow = n + 1;
		String result = "";
		
		int left = 0, right = 0; // [left : right] is the current window
        while (right <= n) {
        	if (numCovered == m) { // all character in t has been covered
        		if (right - left < lenMinWindow) {
        			lenMinWindow = right - left;
        			result = s.substring(left, right);
        		}
        		char c = s.charAt(left);
        		if (charUncovered.containsKey(c)) {
        			charUncovered.put(c, charUncovered.get(c) + 1);
        			if (charUncovered.get(c) > 0) numCovered--;
        		}
        		left++;
        		
        	} else {
        		if (right < n) {
        			char c = s.charAt(right);
        			if (charUncovered.containsKey(c)) {
            			charUncovered.put(c, charUncovered.get(c) - 1);
            			if (charUncovered.get(c) >= 0) numCovered++;
            		}
        		}
        		right++;
        		
        	}
        }
        return result;
    }
	
	public static void main(String [] args){
		String s = "bba";
		String t = "ab";
		System.out.println(new Solution().minWindow(s, t));
	}
}
