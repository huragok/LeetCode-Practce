
public class Solution {
	public int countPrimes(int n) {
		if (n < 3) return 0;
		boolean [] isPrime = new boolean [n];
		isPrime[0] = false; isPrime[1] = false;
		for (int i = 2; i < n; i++) isPrime[i] = true;
		
		for (int p = 2; p * p < n; p++) {
			if (isPrime[p]) {
				for (int i = p * p; i < n; i += p) {
					isPrime[i] = false;
				}
			}
		}
		
		int count = 0;
		for (int i = 0; i < n; i++) {
			if (isPrime[i]) count++;
		}
		return count;
    }
	
	public static void main(String [] args) {
		int n = 100;
		System.out.println(new Solution().countPrimes(n));
	}
}
