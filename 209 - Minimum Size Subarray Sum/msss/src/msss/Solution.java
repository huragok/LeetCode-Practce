package msss;

public class Solution {
	public int minSubArrayLen(int s, int[] nums) {
        int n = nums.length;
        int lenMin = 0;
        
        int start = 0;
        int sum = 0;
        int i;
        for (i = 0; i < n; i++) {
        	sum += nums[i];
        	if (sum >= s) {
        		while (start <= i && sum >= s) {
        			sum -= nums[start];
        			start++;
        		}
        		lenMin = i - start + 2;
        		break;
        	}
        }
        if (lenMin == 0) return 0;
        i++;
        for (; i < n; i++) {
        	sum += nums[i];
        	if (sum >= s) {
        		while (start <= i && sum >= s) {
        			sum -= nums[start];
        			start++;
        		}
        		int lenTmp = i - start + 2;
        		if (lenTmp < lenMin) lenMin = lenTmp;
        	}
        }
        return lenMin;
    }
	
	public static void main(String [] args) {
		int [] nums = {1, 4, 4};
		int s = 4;
		System.out.println(new Solution().minSubArrayLen(s, nums));
	}
}
