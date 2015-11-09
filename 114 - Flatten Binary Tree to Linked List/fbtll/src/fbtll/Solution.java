package fbtll;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public void flatten(TreeNode root) {
        if (root == null) {
        	return;
        } else if (root.left == null) {
        	flatten(root.right);
        } else {
        	TreeNode right = root.right;
        	TreeNode pre = root.left;
        	while (pre.right != null) pre = pre.right;
        	root.right = root.left;
        	root.left = null;
        	pre.right = right;
        	flatten(root.right);
        }
    }
}
