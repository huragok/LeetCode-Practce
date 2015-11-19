package hn;

import java.util.Set;
import java.util.HashSet;

public class Solution {
	public boolean isHappy(int n) {
		Set<Integer> history = new HashSet<Integer> ();
		while (!history.contains(n) && n != 1) {
			history.add(n);
			n = sumSquareDigits(n);
		}
		if (n == 1) {
			return true;
		} else {
			return false;
		}
    }
	
	private int sumSquareDigits(int n) {
		int result = 0;
		while (n > 0) {
			int d = n % 10;
			result += d * d;
			n /= 10;
		}
		return result;
	}
}
