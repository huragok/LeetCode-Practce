package ra;

public class Solution {
	public void rotate(int[] nums, int k) {
        int n = nums.length;
        k %= n;
        reverse(nums, 0, n - k); reverse(nums, n - k, n);
        reverse(nums, 0, n);
    }
	
	private void reverse(int [] nums, int start, int end) {
		int left = start, right = end - 1;
		while (right > left ) {
			int tmp = nums[left];
			nums[left] = nums[right];
			nums[right] = tmp;
			left++; right--;
		}
		return;
	}
}
