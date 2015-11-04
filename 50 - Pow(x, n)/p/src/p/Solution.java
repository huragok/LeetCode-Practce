package p;
public class Solution {
    public double myPow(double x, int n) {
    	boolean nonneg = true;
    	long m = (long) n;
    	if (m == 0) {
    		return 1;
    	} else if (m < 0) {
    		nonneg = false;
    		m = -m;
    	}

		int twoLog = 0;
		long i = 1;
		while (i <= m) {
			i <<= 1;
			twoLog++;
		}
		twoLog--;

		double [] powTwoPower= new double [twoLog + 1];
		powTwoPower[0] = x;
		for (int j = 1; j <= twoLog; j++) {
			powTwoPower[j] = powTwoPower[j - 1] * powTwoPower[j - 1];
		}
		double result = 1.0;
		long residual = m;
		while (residual > 0) {
			long j = 1;
			int pow = 0;
			while (j <= residual) {
				j <<= 1;
				pow++;
			}
			j >>= 1;
			pow--;
			result *= powTwoPower[pow];
			residual -= j;
		}
    	if (nonneg) {
    		return result;
    	} else {
    		return 1 / result;
    	}
    }
    
    public static void main(String [] args) {
    	double x = 1.000000;
    	int n = -2147483648;
    	System.out.println(new Solution().myPow(x, n));
    }
}