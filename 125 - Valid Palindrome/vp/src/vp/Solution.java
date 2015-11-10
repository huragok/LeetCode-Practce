package vp;

public class Solution {
	public boolean isPalindrome(String s) {
        s = s.replaceAll("[^a-zA-Z0-9]", "");
        s = s.toLowerCase();
        System.out.println(s);
        int n = s.length();
        for (int i = 0; i < n / 2; i++) {
        	if (s.charAt(i) != s.charAt(n - 1 - i)) return false;
        }
        return true;
    }
	
	public static void main(String [] args){
		String s = "a.";
		System.out.println(new Solution().isPalindrome(s));
	}
}
