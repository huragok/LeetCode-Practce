package btmps;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	private int result = 0;
	public int maxPathSum(TreeNode root) {
		if (root != null) result = root.val;
		dps(root);
		return result;
        
    }
	
	private int dps(TreeNode root) { // The max sum over a path starting from this root
		if (root == null) return 0;
		int maxSumLeft = dps(root.left);
		int maxSumRight = dps(root.right);
		
		int maxSum = root.val;
		if (maxSumLeft > 0 && maxSumLeft > maxSumRight) {
			maxSum += maxSumLeft;
		} else if (maxSumRight > 0 && maxSumRight > maxSumLeft) {
			maxSum += maxSumRight;
		}
		
		if (maxSum > result) result = maxSum;
		if (root.val + maxSumLeft + maxSumRight > result) result = root.val + maxSumLeft + maxSumRight;
		
		return maxSum;
	}
}
