package ms;

public class Solution {
	public int maxSubArray(int[] nums) {
        int n = nums.length;
       	int maxSum = nums[0];
       	int maxSumTail = nums[0];
       	
       	for (int i = 1; i < n; i++) {
       		if (maxSumTail <= 0) {
       			maxSumTail = nums[i];
       		} else {
       			maxSumTail += nums[i];
       		}
       		maxSum = maxSum > maxSumTail ? maxSum : maxSumTail;
       	}
       	return maxSum;
        
    }
	
	public static void main(String [] args) {
		int [] nums = {-2,1,-3,4,-1,2,1,-5,4};
		System.out.println(new Solution().maxSubArray(nums));
	}
}
