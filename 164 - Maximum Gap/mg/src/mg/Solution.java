package mg;

import java.util.Arrays;

public class Solution {
	public int maximumGap(int[] nums) {
        int n = nums.length;
        if (n < 2) return 0;
        int min = nums[0]; int max = nums[0];
        for (int num: nums) {
        	if (num < min) min = num;
        	if (num > max) max = num;
        }
        
        int [] bucketMin = new int [n];
        int [] bucketMax = new int [n];
        boolean [] bucketEmpty = new boolean [n];
        for (int i = 0; i < n; i++) bucketEmpty[i] = true;
        double bucketSize = (double)(max - min) / (n - 1);
        if (bucketSize < 1.0) bucketSize = 1.0;
        
        for (int num: nums) {
        	int bucketIdx = (int)((num - min) / bucketSize);
        	if (bucketEmpty[bucketIdx] || bucketMin[bucketIdx] > num) bucketMin[bucketIdx] = num;
        	if (bucketEmpty[bucketIdx] || bucketMax[bucketIdx] < num) bucketMax[bucketIdx] = num;
        	bucketEmpty[bucketIdx] = false;
        }
        
        int i = 0;
        for (; i < n - 1; i++) {
        	if (!bucketEmpty[i]) break;
        }
        int maxGap = 0;
        for (int j = i + 1; j < n; j++) {
        	if (!bucketEmpty[j]) {
        		if (bucketMin[j] - bucketMax[i] > maxGap) maxGap = bucketMin[j] - bucketMax[i];
        		i = j;
        	}
        }
        return maxGap;
	}
	
	public static void main(String [] args) {
		int [] nums = {3, 6, 9, 1};
		System.out.println(new Solution().maximumGap(nums));
	}
}
