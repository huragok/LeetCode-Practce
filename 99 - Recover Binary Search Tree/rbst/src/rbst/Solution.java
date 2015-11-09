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
        		
        	} else {
        		TreeNode p = curr.left;
        		while (p.right != null && p.right != curr) p = p.right;
        		if (p.right == null) {
        			p.right = curr;
        			curr = curr.left;
        		} else {
        			p.right = null;
        			pre = curr;
        			curr = curr.right;
        		}
        	}
        	
        	if (pre != null && curr != null && pre.val > curr.val) {
    			if (first == null) {
    				first = pre;
    			}
    			second = curr;
    		}
        }
        
        int tmp = first.val;
        first.val = second.val;
        second.val = tmp;
        return;
        
    }
}
