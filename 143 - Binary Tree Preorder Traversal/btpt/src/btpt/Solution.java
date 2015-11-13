package btpt;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public List<Integer> preorderTraversal(TreeNode root) {
		List<Integer> result = new ArrayList<Integer> ();
		TreeNode curr = root;
		while (curr != null) {
			if (curr.left == null) {
				result.add(curr.val);
				curr = curr.right;
			} else {
				TreeNode pre = curr.left;
				while (pre.right != null && pre.right != curr) pre = pre.right;
				if (pre.right == null) {
					result.add(curr.val);
					pre.right = curr;
					curr = curr.left;
				} else {
					pre.right = null;
					curr = curr.right;
				}
			}
		}
		return result;
    }
}
