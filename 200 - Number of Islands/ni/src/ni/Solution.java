package ni;

public class Solution {

	private char [][] grid;
	private int m, n;
	public int numIslands(char[][] grid) {
        this.grid = grid;
        this.m = grid.length;
        if (m == 0) return 0;
        this.n = grid[0].length;
        
        int count = 0;
        for (int row = 0; row < m; row++) {
        	for (int col = 0; col < n; col++) {
        		if (grid[row][col] == '1') {
        			dfs(row, col);
        			count++;
        		}
        	}
        }
        return count;
    }
	
	private void dfs(int row, int col) {
		if (row < 0 || row >= m) return;
		if (col < 0 || col >= n) return;
		
		if (grid[row][col] == '0') return;
		
		grid[row][col] = '0';
		dfs(row - 1, col);
		dfs(row + 1, col);
		dfs(row, col - 1);
		dfs(row, col + 1);
	}
}
