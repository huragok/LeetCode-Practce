package mdbt;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public int maxDepth(TreeNode root) {
        if (root == null) {
        	return 0;
        } else {
        	int depthLeft = maxDepth(root.left);
        	int depthRight = maxDepth(root.right);
        	return (depthLeft > depthRight ? depthLeft : depthRight) + 1;
        }
    }
}
