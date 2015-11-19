package bandnr;

public class Solution {
	public int rangeBitwiseAnd(int m, int n) {
        int mxorn = m ^ n;
        int shift = 0;
        for (int i = 0; i < 32; i++) {
        	if ((mxorn & 1) == 1) {
        		shift = i;
        	}
        	mxorn >>= 1;
        }
        return (m >> shift) << shift;
    }
	
	public static void main(String [] args) {
		int m = 5, n = 7;
		System.out.println(new Solution().rangeBitwiseAnd(m, n));
	}
}
