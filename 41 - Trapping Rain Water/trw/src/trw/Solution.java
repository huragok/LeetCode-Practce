package trw;

public class Solution {
    public int trap(int[] height) {
    	int n = height.length;
    	int left = 0, right = n - 1;
    	int h = 0;
    	int volume = 0;
    	
    	while (left < right) {
    		if (height[left] < height[right]) {
    			h = h > height[left] ? h : height[left];
    			volume += h - height[left];
    			left++;
    		} else {
    			h = h > height[right] ? h : height[right];
    			volume += h - height[right];
    			right--;
    		}
    	}
        return volume;
    }
}
