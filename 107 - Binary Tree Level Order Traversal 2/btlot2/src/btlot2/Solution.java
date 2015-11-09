package btlot2;

import java.util.List;
import java.util.LinkedList;
import java.util.Queue;


public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public List<List<Integer>> levelOrderBottom(TreeNode root) {
		List<List<Integer>> result = new LinkedList<List<Integer>> ();
		if (root == null) return result;
		Queue<TreeNode> q = new LinkedList<TreeNode> ();
		q.add(root);
		Queue<TreeNode> qNew = new LinkedList<TreeNode> ();
		List<Integer> level = new LinkedList<Integer> ();
		while (!q.isEmpty()) {
			TreeNode node = q.poll();
			level.add(node.val);
			if (node.left != null) qNew.add(node.left);
			if (node.right != null) qNew.add(node.right);
			
			if (q.isEmpty()) {
				q = qNew;
				qNew = new LinkedList<TreeNode> ();
				result.add(0, level);
				level = new LinkedList<Integer> ();
			}
		}
		return result;
    }
}
