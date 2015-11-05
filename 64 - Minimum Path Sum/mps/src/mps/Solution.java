package mps;

public class Solution {
	public int minPathSum(int[][] grid) {
        int m = grid.length;
        if (m == 0) return 0;
        int n = grid[0].length;
        if (n == 0) return 0;
        
        int [] sum = new int [n];
        sum[0] = grid[0][0];
        for (int col = 1; col < n; col++) {
        	sum[col] = sum[col - 1] + grid[0][col];
        }
        
        for (int row = 1; row < m; row++) {
        	sum[0] += grid[row][0];
        	for (int col = 1; col < n; col++) {
        		sum[col] = (sum[col] > sum[col - 1] ? sum[col - 1] : sum[col]) + grid[row][col];
        	}
        }
        
        return sum[n - 1];
    }
}
