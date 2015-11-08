package rdsa;
import java.util.Arrays;
public class Solution {
	public int removeDuplicates(int[] nums) {
        int n = nums.length;
        int countLastVal = 0;
        int lastVal = 0;
        int ptrRemoved = -1;
        for (int i = 0; i < n; i++) {
        	if (countLastVal == 0 || nums[i] != lastVal) {
        		lastVal = nums[i];
        		countLastVal = 1;
        		ptrRemoved++;
        		nums[ptrRemoved] = nums[i];
        	} else if (countLastVal == 1) {
        		countLastVal = 2;
        		ptrRemoved++;
        		nums[ptrRemoved] = nums[i];
        	} 
        }
        return ptrRemoved + 1;
    }
	
	public static void main(String [] args) {
		int [] nums = {1,1,1,2,2,3};
		System.out.println(new Solution().removeDuplicates(nums));
		System.out.println(Arrays.toString(nums));
	}
}
