package srln;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	private int result;
	private int sumPath;
	public int sumNumbers(TreeNode root) {
        result = 0;
        sumPath = 0;
        
        if (root != null) {
        	dfs(root);
        }
        return result;
    }
	
	private void dfs(TreeNode root) {
		sumPath = sumPath * 10 + root.val;
		if (root.left == null && root.right == null) result += sumPath;
		
		if (root.left != null) dfs(root.left);
		if (root.right != null) dfs(root.right);
		
		sumPath = (sumPath - root.val) / 10;
	}
}
