package lrh;

import java.util.Stack;

public class Solution {
	public int largestRectangleArea(int[] height) {
        int n = height.length;
        
        Stack<Integer> idx = new Stack<Integer> ();
        
        int maxArea = 0;
        for (int i = 0; i <= n; i++) {
        	int h = (i == n) ? 0 : height[i];
	        if (idx.isEmpty() || h >= height[idx.peek()]) {
	        		idx.push(i);
        	} else {
        		while (!idx.isEmpty() && h < height[idx.peek()]) {
        			int idxTmp = idx.pop();
        			int hTop = height[idxTmp];
        			
	        		int width;
	        		if (idx.isEmpty()) {
	        			width = i;
	        		} else {
	        			width = i - 1 - idx.peek();
	        		}
	        			
	        		maxArea = (maxArea > hTop * width ? maxArea : hTop * width);

	        	}
        		idx.push(i);
        	}
        }
		
		return maxArea;
    }
}
