package sm2;

public class Solution {
    public int[][] generateMatrix(int n) {
        int [][] result = new int [n][n];
        int v = 0;
        int left = 0, right = n - 1;
        int top = 0, bottom = n - 1;
        while (right - left >= 0) {
        	if (right - left > 0) {
        		for (int col = left; col < right; col++) {
        			v++;
        			result[top][col] = v;
        		}
        		for (int row = top; row < bottom; row++) {
        			v++;
        			result[row][right] = v;
        		}
        		for (int col = right; col > left; col--) {
        			v++;
        			result[bottom][col] = v;
        		}
        		for (int row = bottom; row > top; row--) {
        			v++;
        			result[row][left] = v;
        		}
        		left++; right--;
        		top++; bottom--;
        	} else {
        		v++;
        		result[top][left] = v;
        		break;
        	}
        }
        return result;
    }
}
