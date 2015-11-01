package ri;

public class Solution {
	public int reverse(int x) {
        int sign = x >= 0 ? 1 : -1;
        x = x * sign;
        int original = x;
        int reversed = 0;
        while (x > 0) {
        	reversed = reversed * 10 + x % 10;
        	x /= 10;
        }
        
        int result = reversed * sign;
        
        x = reversed;
        reversed = 0;
        while (x > 0) {
        	reversed = reversed * 10 + x % 10;
        	x /= 10;
        }
        
        while (original > 0 && original % 10 == 0) {
        	original /= 10;
        }
        if (reversed == original) {
        	return result;
        } else {
        	return 0;
        }
    }
	
	static public void main(String [] args) {
		int x = 10;
		System.out.println((new Solution()).reverse(x));
	}
}
