package rws2;

import java.util.Arrays;

public class Solution {
	public void reverseWords(char[] s) {
        int n = s.length;
        int wordStart = 0;
        for (int i = 0; i < n; i++) {
        	if (s[i] == ' ') {
        		reverseWords(s, wordStart, i);
        		wordStart = i + 1;
        	}
        }
        reverseWords(s, wordStart, n);
        reverseWords(s, 0, n);
    }
	
	// reverse s[start : end]
	private void reverseWords(char[] s, int start, int end) {
		int left = start, right = end - 1;
		while (right > left) {
			char tmp = s[left];
			s[left] = s[right];
			s[right] = tmp;
			left++; right--;
		}
	}
	
	public static void main(String [] args) {
		char [] s = {'t','h','e',' ','s','k','y',' ','i','s',' ','b','l','u','e'};
		new Solution().reverseWords(s);
		System.out.println(Arrays.toString(s));
	}
}
