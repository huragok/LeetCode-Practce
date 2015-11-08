package vbst;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public boolean isValidBST(TreeNode root) {
        return isValidBST(root, 0, 0, false, false);
    }
	
	private boolean isValidBST(TreeNode root, int lb, int ub, boolean useLb, boolean useUb) {
		if (root == null) return true;
		
		boolean validRoot = (!useLb || lb < root.val) && (!useUb || ub > root.val);
		if (!validRoot) return false;
		
		return isValidBST(root.left, lb, root.val, useLb, true) && isValidBST(root.right, root.val, ub, true, useUb);
	}
}
