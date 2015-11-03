package vs;

public class Solution {
    public boolean isValidSudoku(char[][] board) {
        int [] prime = new int [] {1, 2, 3, 5, 7, 11, 13, 17, 19, 23};
        int [] prodRow = new int [] {1, 1, 1, 1, 1, 1, 1, 1, 1};
        int [] prodCol = new int [] {1, 1, 1, 1, 1, 1, 1, 1, 1};
        int [] prodSq = new int [] {1, 1, 1, 1, 1, 1, 1, 1, 1};
        
        for (int i = 0; i < 9; i++) {
        	for (int j = 0; j < 9; j++) {
        		char s = board[i][j];
        		if (s != '.') {
        			int p = prime[Character.getNumericValue(s)];
        			if (prodRow[i] % p == 0 || prodCol[j] % p ==0 || prodSq[(i / 3) * 3 + (j / 3)] % p == 0) {
        				System.out.println(p);
        				System.out.println(prodRow[i]);
        				System.out.println("_____");
        				System.out.println(prodCol[j]);
        				System.out.println("_____");
        				System.out.println(prodSq[(i / 3) * 3 + (j / 3)]);
        				System.out.println("_____");
        				System.out.println(i);System.out.println(j);
        				return false;
        			}
        			prodRow[i] *= p; prodCol[j] *= p; prodSq[(i / 3) * 3 + (j / 3)] *= p;
        		}
        	}
        }
        return true;
    }
    
    public static void main(String [] args) {
    	char [][] board = new char [9][];
    	board[0] = new char [] {'.', '8', '7', '6', '5', '4', '3', '2', '1'};
    	board[1] = new char [] {'2', '.', '.', '.', '.', '.', '.', '.', '.'};
    	board[2] = new char [] {'3', '.', '.', '.', '.', '.', '.', '.', '.'};
    	board[3] = new char [] {'4', '.', '.', '.', '.', '.', '.', '.', '.'};
    	board[4] = new char [] {'5', '.', '.', '.', '.', '.', '.', '.', '.'};
    	board[5] = new char [] {'6', '.', '.', '.', '.', '.', '.', '.', '.'};
    	board[6] = new char [] {'7', '.', '.', '.', '.', '.', '.', '.', '.'};
    	board[7] = new char [] {'8', '.', '.', '.', '.', '.', '.', '.', '.'};
    	board[8] = new char [] {'9', '.', '.', '.', '.', '.', '.', '.', '.'};
    	
    	System.out.println(new Solution().isValidSudoku(board));
    }
}
