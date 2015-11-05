package cs;
import java.lang.Math;
public class Solution {
	public int climbStairs(int n) {
        double r1 = (1.0 + Math.sqrt(5.0)) / 2.0;
        double r2 = (1.0 - Math.sqrt(5.0)) / 2.0;
        double a = (5.0 + 3.0 * Math.sqrt(5.0)) / 10.0;
        double b = (5.0 - 3.0 * Math.sqrt(5.0)) / 10.0;
        return (int) (a * Math.pow(r1, n - 1) + b * Math.pow(r2, n - 1) + 0.1);
    }
	
	public static void main (String [] args) {
		int n = 3;
		System.out.println(new Solution().climbStairs(n));
	}
}
