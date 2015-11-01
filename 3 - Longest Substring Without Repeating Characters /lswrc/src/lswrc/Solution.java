package lswrc;
import java.util.*;

public class Solution {
	public int lengthOfLongestSubstring(String s) {
		Map<Character, Integer> map = new HashMap<Character, Integer>(26);
        int start = 0;
        int maxLen = 0;
        for (int idx = 0; idx < s.length(); idx++) {
        	char c = s.charAt(idx);
        	if (map.containsKey(c) && map.get(c) >= start) {
        		if (idx - start > maxLen) {
        			maxLen = idx - start;
        		}
        		start = map.get(c) + 1;
        	}
        	map.put(c, idx);
        }
        int lenTail = s.length() - start;
        if (lenTail > maxLen) {
        	maxLen = lenTail;
        }
        return maxLen;
    }
	
	static public void main(String [] args) {
		String s = "abcabcbbb";
		Solution sol = new Solution();
		System.out.println(sol.lengthOfLongestSubstring(s));
	}
}
