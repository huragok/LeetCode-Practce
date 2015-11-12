package sr;


public class Solution {
	
	private char[][] board;
	private int m, n;
	public void solve(char[][] board) {
        m = board.length;
        if (m == 0) return;
        n = board[0].length;
        if (n == 0) return;
        this.board = board;
        
        for (int row = 0; row < m; row++) {
        	for (int col = 0; col < n; col++) {
        		if (board[row][col] == 'O') board[row][col] = 'U';
        	}
        }
        

        // Mark the 'O''s at the 4 edges of the board
        for (int row = 0; row < m; row++) {
    		dfs(row, 0);
    		dfs(row, n - 1);
        }
        
        for (int col = 0; col < n; col++) {
    		dfs(0, col);
    		dfs(m - 1, col);
        }
        
        
        
        // The left 'U' grids are not connected to any 'O' nodes on the edge of the board
        for (int row = 0; row < m; row++) {
        	for (int col = 0; col < n; col++) {
        		if (board[row][col] == 'U') {
        			board[row][col] = 'X';
        		}
        	}
        }
        
        return;
    }
	
	private void dfs(int row, int col) {
		if (row < 0 || row >= m || col < 0 || col >= n) return;
		if (board[row][col] != 'U') return;
		board[row][col] = 'O';
		dfs(row + 1, col);
		dfs(row - 1, col);
		dfs(row, col + 1);
		dfs(row, col - 1);
		return;
	}
}
