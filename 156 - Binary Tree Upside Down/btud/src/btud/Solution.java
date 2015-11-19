package btud;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public TreeNode upsideDownBinaryTree(TreeNode root) {
        if (root == null || root.left == null) return root;
        
        TreeNode rootLeft = upsideDownBinaryTree(root.left);
        
        TreeNode curr = rootLeft;
        while (curr.right != null) curr = curr.right;
        curr.right = root;
        curr.left = root.right;
        root.left = null; root.right = null;
        return rootLeft;
    }
}
