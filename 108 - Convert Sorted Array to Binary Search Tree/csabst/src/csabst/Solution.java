package csabst;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public TreeNode sortedArrayToBST(int[] nums) {
		int n = nums.length;
		return sortedArrayToBST(nums, 0, n);
    }
	
	private TreeNode sortedArrayToBST(int[] nums, int l, int u) {
		if (u <= l) return null;
		
		int m = (l + u) / 2;
		TreeNode root = new TreeNode (nums[m]);
		root.left = sortedArrayToBST(nums, l, m);
		root.right = sortedArrayToBST(nums, m + 1, u);
		return root;
	}
}
