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
	
	public List<Integer> postorderTraversal(TreeNode root) {
		List<Integer> result = new ArrayList<Integer> ();
		TreeNode anchor = new TreeNode(0);
		anchor.left = root;
		TreeNode curr = anchor;
		while (curr != null) {
			if (curr.left == null) {
				curr = curr.right;
			} else{
				TreeNode pre = curr.left;
				while (pre.right != null && pre.right != curr) pre = pre.right;
				if (pre.right == null) {
					pre.right = curr;
					curr = curr.left;
				} else {
					reverseOutput(curr.left, pre, result);
					pre.right = null;
					curr = curr.right;
				}
			}
		}
		return result;
        
    }
	
	private void reverseOutput(TreeNode top, TreeNode bottom, List<Integer> result) {
		TreeNode ptr = top;
		List<Integer> tmp = new ArrayList<Integer> ();
		while (ptr != bottom) {
			tmp.add(0, ptr.val);
			ptr = ptr.right;
		}
		tmp.add(0, bottom.val);
		result.addAll(tmp);
		return;
	}
}
