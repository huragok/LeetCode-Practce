package st;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null ^ q == null) return false;
        if (p == null && q == null) return true;
        if (p.val == q.val) {
        	return isSameTree(p.left, q.left) && isSameTree(p.right, q.right);
        } else {
        	return false;
        }
    }	
}
