package ws;

public class Solution {
	private int m, n, l;
	String word;
	
	public boolean exist(char[][] board, String word) {
		m = board.length;
		n = board[0].length;
		l = word.length();
		this.word = word;
		
		for (int i = 0; i < m; i++) {
			for (int j = 0; j < n; j++) {
				if (existFrom(board, i, j, 0)) {
					return true;
				}
			}
		}
        return false;
    }
	
	private boolean existFrom(char[][] board, int row, int col, int idx) {
        if (idx == l) {
        	return true;
        } else if (row < 0 || row >= m || col < 0 || col >= n) {
        	return false;
        } else if (board[row][col] != word.charAt(idx)){
        	return false;
        } else {
        	board[row][col] = '@';
        	if (existFrom(board, row - 1, col, idx + 1) || existFrom(board, row + 1, col, idx + 1) ||
        		existFrom(board, row, col - 1, idx + 1) || existFrom(board, row, col + 1, idx + 1)) {
        		return true;
        	} else {
        		board[row][col] = word.charAt(idx);
        		return false;
        	}
        }
    }
	
	public static void main (String [] args) {
		char [][] board = {{'A','B','C','E'},
		                   {'S','F','C','S'},
		                   {'A','D','E','E'}};
		String word = "ABCB";
		System.out.println(new Solution().exist(board, word));
	}
}
