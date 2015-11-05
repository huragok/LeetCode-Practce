package sm;

import java.util.List;
import java.util.LinkedList;

public class Solution {
	public List<Integer> spiralOrder(int[][] matrix) {
		int m = matrix.length;
		if (m == 0) {
			return new LinkedList<Integer> ();
		}
		int n = matrix[0].length;
		if (n == 0) {
			return new LinkedList<Integer> ();
		}
		int left = 0, right = n - 1;
		int top = 0, bottom = m - 1;
		
		List<Integer> result = new LinkedList<Integer> ();
		while (left <= right && top <= bottom) {
			if (left < right && top < bottom) {
				for (int col = left; col < right; col++) {
					result.add(matrix[top][col]);
				}
				for (int row = top; row < bottom; row++) {
					result.add(matrix[row][right]);
				}
				for (int col = right; col > left; col--) {
					result.add(matrix[bottom][col]);
				}
				for (int row = bottom; row > top; row--) {
					result.add(matrix[row][left]);
				}
				left++; right--;
				top++; bottom--;
			} else if (left == right) {
				for (int row = top; row <= bottom; row++) {
					result.add(matrix[row][left]);
				}
				break;
			} else {
				for (int col = left; col <= right; col++) {
					result.add(matrix[top][col]);
				}
				break;
			}
		}
		return result;
    }
}
