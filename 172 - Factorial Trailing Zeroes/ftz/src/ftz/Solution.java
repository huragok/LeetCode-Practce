package ftz;

public class Solution {
	public int trailingZeroes(int n) {
        long power5 = 5;
        int count5 = 0;
        while (power5 <= n) {
        	count5 += n / power5;
        	power5 *= 5;
        }
        
        long power2 = 2;
        int count2 = 0;
        while (power2 <= n) {
        	count2 += n / power2;
        	power2 *= 2;
        }
        
        return count2 > count5 ? count5 : count2;
    }
}
