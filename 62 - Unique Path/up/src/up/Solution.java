package up;

public class Solution {
	public int uniquePaths(int m, int n) {
        if (m == 0 || n == 0) {
        	return 0;
        }
        
        int [] count = new int [n];
        for (int col = 0; col < n; col++) {
        	count[col] = 1;
        }
        for (int row = 1; row < m; row++) {
        	count[0] = 1;
        	for (int col = 1; col < n; col++) {
        		count[col] += count[col - 1];
        	}
        }
        
        return count[n - 1];
    }
	
}
