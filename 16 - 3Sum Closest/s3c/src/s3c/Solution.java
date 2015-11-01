package s3c;
import java.util.*;

public class Solution {
	public int threeSumClosest(int[] nums, int target) {
		Arrays.sort(nums);
		int minDist = Math.abs(nums[0] + nums[1] + nums[2] - target);
		int sign = nums[0] + nums[1] + nums[2] - target > 0 ? 1 : -1;
		
		int i = 0;
		while (i < nums.length - 2) {
			int j = i + 1;
			int k = nums.length - 1;
			int residual = target - nums[i];
			
			while (k > j) {
				int dist = nums[k] + nums[j] - residual;
				if (dist > minDist) {
					k--;
				} else if (dist < -minDist) {
					j++;
				} else {
					//System.out.println(Arrays.toString(new int [] {nums[i], nums[j], nums[k]}));
					minDist = Math.abs(dist);
					sign = dist > 0 ? 1 : -1;
					if (dist > 0)
						k--;
					else
						j++;
					if (minDist == 0) {
						return target;
					}
				}
			}
			i++;
		}
		return target + sign * minDist;
        
    }
	
	public static void main(String [] args) {
		int [] nums = {-3, -2, -5, 3, -4};
		int target = -1;
		System.out.println(new Solution().threeSumClosest(nums, target));
	}
}
