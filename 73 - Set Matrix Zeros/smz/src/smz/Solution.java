package smz;

public class Solution {
	public void setZeroes(int[][] matrix) {
        int m = matrix.length;
        if (m == 0) return;
        int n = matrix[0].length;
        if (n == 0) return;
        
        boolean rowTop = false;
        for (int col = 0; col < n; col++) {
        	if (matrix[0][col] == 0) {
        		rowTop = true;
        		break;
        	}
        }
        
        boolean colLeft = false;
        for (int row = 0; row < m; row++) {
        	if (matrix[row][0] == 0) {
        		colLeft = true;
        		break;
        	}
        }
        
        for (int row = 1; row < m; row++) {
        	for (int col = 1; col < n; col++) {
        		if (matrix[row][col] == 0) {
        			matrix[row][0] = 0;
        			matrix[0][col] = 0;
        		}
        	}
        }
        
        for (int row = 1; row < m; row++) {
        	if (matrix[row][0] == 0) {
        		for (int col = 1; col < n; col++) {
        			matrix[row][col] = 0;
        		}
        	}
        }
        
        for (int col = 1; col < n; col++) {
        	if (matrix[0][col] == 0) {
        		for (int row = 1; row < m; row++) {
        			matrix[row][col] = 0;
        		}
        	}
        }
        
        if (rowTop) {
        	for (int col = 0; col < n; col++) {
        		matrix[0][col] = 0;
        	}
        }
        
        if (colLeft) {
        	for (int row = 0; row < m; row++) {
        		matrix[row][0] = 0;
        	}
        }
        
        return;
    }
}
