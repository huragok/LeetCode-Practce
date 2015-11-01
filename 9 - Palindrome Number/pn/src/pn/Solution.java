package pn;

public class Solution {
	public boolean isPalindrome(int x) {
		if (x < 0) {
			return false;
		}
		int original = x;
		int reverse = 0;
		while (x > 0) {
			reverse = reverse * 10 + x % 10;
			x /= 10;
		}
		return original == reverse;
    }

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int x = 12321;
		Solution sol = new Solution();
		System.out.println(sol.isPalindrome(x));
	}

}
