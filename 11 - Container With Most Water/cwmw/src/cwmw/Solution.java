package cwmw;

public class Solution {
	public int maxArea(int[] height) {
        int n = height.length;
        
        int left = 0;
        int right = n - 1;
        
        int maxVolume = 0;
        int v = 0;
        while (left < right) {
        	if (height[left] <= height[right]) {
        		v = height[left] * (right - left);
        		left += 1;
        	} else {
        		v = height[right] * (right - left);
        		right -= 1;
        	}
        	if (v > maxVolume) {
        		maxVolume = v;
        	}
        }
        return maxVolume;
    }
}
