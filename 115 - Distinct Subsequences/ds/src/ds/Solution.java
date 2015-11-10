package ds;

public class Solution {
	public int numDistinct(String s, String t) {
		int m = s.length(), n = t.length();
		
		int [] count = new int [m + 1];
		//j = 1
		count[0] = 0;
		for (int i = 1; i <= m; i++) {
			count[i] = (s.charAt(i - 1) == t.charAt(0) ? 1 : 0);
		}
        
		for (int j = 2; j <= n; j++){
			int countCumSum = 0;
			for (int i = 1; i <= m; i++) {
				int tmp = count[i];
				if (s.charAt(i - 1) == t.charAt(j - 1)) {
					count[i] = countCumSum;
				} else {
					count[i] = 0;
				}
				countCumSum += tmp;
			}
			
		}
		for (int i = 1; i <= m; i++) {
			count[i] += count[i - 1];
		}
		return count[m];
    }
}
