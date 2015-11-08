package mr;

import java.util.Arrays;
import java.util.Stack;

public class Solution {
	public int maximalRectangle(char[][] matrix) {
		int m = matrix.length;
        if (m == 0) return 0;
        int n = matrix[0].length;
        if (n == 0) return 0;
        
        int largestArea = 0;
        int [] hist = new int [n];
        for (int row = 0; row < m; row++){
        	for (int col = 0; col < n; col++) {
        		hist[col] = (matrix[row][col] == '1') ? hist[col] + 1 : 0;
        	}
        	int largestAreaRow = largestRectangleArea(hist);
        	largestArea = (largestAreaRow > largestArea) ? largestAreaRow : largestArea;
        }
        
        return largestArea;
    }
	
	private int largestRectangleArea(int [] hist) {
		int n = hist.length;
		Stack<Integer> idxStack = new Stack<Integer> ();
		
		int largestArea = 0;
		for (int i = 0; i <= n; i++) {
			int h = (i < n) ? hist[i] : 0;
			if (idxStack.isEmpty() || hist[idxStack.peek()] <= h) {
				idxStack.push(i);
			} else {
				int width = 0;
				while (!idxStack.isEmpty() && hist[idxStack.peek()] > h) {
					int idx = idxStack.pop();
					
					int height = hist[idx];
					if (idxStack.isEmpty()) {
						width = i;
					} else {
						width = i - 1 - idxStack.peek();
					}
					largestArea = (largestArea > height * width) ? largestArea : height * width;
				}
				idxStack.push(i);
			}
		}
		return largestArea;
	}
	
	public static void main(String [] args) {
		char [][] matrix = new char [][] {{'1'}};
		System.out.println(new Solution().maximalRectangle(matrix));
	}
}
