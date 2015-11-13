package sn2;

import java.util.Arrays;

public class Solution {
	public int singleNumber(int[] nums) {
		int [] countOnes = new int [32];
		for (int i = 0; i < 32; i++) {
			countOnes[i] = 0;
		}
		for (int num: nums) {
			for (int i = 0; i < 32; i++) {
				countOnes[i] += num & 1;
				num >>= 1;
			}
		}
		
		System.out.println(Arrays.toString(countOnes));
		int result = 0;
		for (int i = 31; i >= 0; i--) {
			if (countOnes[i] % 3 != 0) {
				result = (result << 1) + 1;
			} else {
				result <<= 1;
			}
			System.out.println(result);
		}
		return result;
    }
	
	public static void main(String [] args) {
		int [] nums = {2, 2, 3, 2};
		System.out.println(new Solution().singleNumber(nums));
	}
}
