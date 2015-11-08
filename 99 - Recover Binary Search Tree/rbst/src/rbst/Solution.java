package rbst;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public void recoverTree(TreeNode root) {
		TreeNode pre = null;
		TreeNode curr = root;
		TreeNode first = null;
		TreeNode second = null;
        while (curr != null) {
        	
        	if (curr.left == null) {
        		pre = curr;
        		curr = curr.right;
        		if (pre != null && curr != null && pre.val > curr.val) {
        			if (first == null) {
        				first = pre;
        			}
        			second = curr;
        		}
        	} else {
        		pre = curr.left;
        		while (pre.right != null && pre.right != curr) pre = pre.right;
        		if (pre.right == null) {
        			if (pre != null && curr != null && pre.val > curr.val) {
            			if (first == null) {
            				first = pre;
            			}
            			second = curr;
            		}
        			pre.right = curr;
        			curr = curr.left;
        		} else {
        			pre.right = null;
        			pre = curr;
        			curr = curr.right;
        			if (pre != null && curr != null && pre.val > curr.val) {
            			if (first == null) {
            				first = pre;
            			}
            			second = curr;
            		}
        		}
        	}
        }
        
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
        return;
        
    }
}
