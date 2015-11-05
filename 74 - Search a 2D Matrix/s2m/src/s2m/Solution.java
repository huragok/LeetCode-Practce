package s2m;

public class Solution {
	public boolean searchMatrix(int[][] matrix, int target) {
        int m = matrix.length;
        if (m == 0) return false;
        int n = matrix[0].length;
        if (n == 0) return false;
        
        int top = 0, bottom = m;
        if (matrix[0][0] > target) {
        	return false;
        }
        while (bottom - top > 1) {
        	int mid = (top + bottom) / 2;
        	if (matrix[mid][0] <= target) {
        		top = mid;
        	} else {
        		bottom = mid;
        	}
        }
        int row = top;
        
        int left = 0, right = n;
        while (right - left > 1) {
        	int mid = (left + right) / 2;
        	if (matrix[row][mid] <= target) {
        		left = mid;
        	} else {
        		right = mid;
        	}
        }
        
        return matrix[row][left] == target;
    }
}
