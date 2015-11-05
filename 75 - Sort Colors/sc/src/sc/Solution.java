package sc;

public class Solution {
	public void sortColors(int[] nums) {
        int n = nums.length;
        
        int tailRed = -1;
        for (int i = 0; i < n; i++) {
        	if (nums[i] == 0) {
        		tailRed++;
        		int tmp = nums[tailRed];
        		nums[tailRed] = 0;
        		nums[i] = tmp;
        	}
        }
        
        int headBlue = n;
        for (int i = n - 1; i > tailRed; i--) {
        	if (nums[i] == 2) {
        		headBlue--;
        		int tmp = nums[headBlue];
        		nums[headBlue] = 2;
        		nums[i] = tmp;
        	}
        }
        
        return;
    }
}
