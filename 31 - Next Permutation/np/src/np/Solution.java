package np;

import java.util.Arrays;

public class Solution {
	public void nextPermutation(int[] nums) {
        int n = nums.length;
        if (n == 1) {
        	return;
        }
        
        int i = 0;
        for (i = n - 1; i > 0; i--) {
        	if (nums[i - 1] < nums[i]) {
        		break;
        	}
        }
        if (i == 0){ // nums already in a non-increasing order
        	for (int j = 0; j < n / 2; j++) {
        		int tmp = nums[j];
        		nums[j] = nums[n - 1 - j];
        		nums[n - 1 - j] = tmp;
        	}
        	return;
        } else {
        	int j = i;
        	while (j < n && nums[j] > nums[i - 1]) {
        		j++;
        	}
        	int tmp = nums[i - 1];
        	nums[i - 1] = nums[j - 1];
        	nums[j - 1] = tmp;
        	
        	for (int k = i; k < i + (n - i) / 2; k++) {
        		tmp = nums[k];
        		nums[k] = nums[n - 1 - k + i];
        		nums[n - 1 - k + i] = tmp;
        	}
        }
    }
	
	public static void main(String [] args) {
		int [] nums = {1,5,1};
		new Solution().nextPermutation(nums);
		System.out.println(Arrays.toString(nums));
	}
}
