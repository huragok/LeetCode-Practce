package lcp;

public class Solution {
	public String longestCommonPrefix(String[] strs) {
		int n = strs.length;
		if (n == 0) {
			return "";
		}
        
		int minLen = strs[0].length();
		for (String str: strs) {
			if (str.length() < minLen) {
				minLen = str.length();
			}
		}
		
		for (int i = 0; i < minLen; i++) {
			char c = strs[0].charAt(i);
			for (String str: strs) {
				if (str.charAt(i) != c) {
					return strs[0].substring(0, i);
				}
			}
		}
		return strs[0].substring(0, minLen);
    }
	
	public static void main(String [] args) {
		String [] strs = {"abc", "abcd", "ab"};
		System.out.println((new Solution().longestCommonPrefix(strs)));
	}
}
