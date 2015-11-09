package bbt;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	boolean isBalanced;
	public boolean isBalanced(TreeNode root) {
		isBalanced = true;
		depth(root);
        return isBalanced;
    }
	
	private int depth(TreeNode root) {
		if (root == null) return 0;
		
		int depthLeft = depth(root.left);
		int depthRight = depth(root.right);
		
		if (depthLeft - depthRight > 1 || depthLeft - depthRight < -1) isBalanced = false;
		
		return (depthLeft > depthRight ? depthLeft : depthRight) + 1;	
	}
}
