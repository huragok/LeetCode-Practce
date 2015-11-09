package ps;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	private int sumPartial = 0;
	public boolean hasPathSum(TreeNode root, int sum) {
		if (root == null) return false;
		sumPartial += root.val;
		boolean result;
		if (root.left == null && root.right == null) {
			result = (sumPartial == sum);
		} else {
			result = (root.left != null && hasPathSum(root.left, sum)) ||
							 (root.right != null && hasPathSum(root.right, sum));
		}
		sumPartial -= root.val;
		return result;
    }
}
