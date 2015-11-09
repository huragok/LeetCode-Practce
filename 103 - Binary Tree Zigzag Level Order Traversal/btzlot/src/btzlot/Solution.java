package btzlot;

import java.util.Stack;
import java.util.List;
import java.util.LinkedList;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public List<List<Integer>> zigzagLevelOrder(TreeNode root) {
        List<List<Integer>> result = new LinkedList<List<Integer>> ();
		if (root == null) return result;
		Stack<TreeNode> s = new Stack<TreeNode> ();
		Stack<TreeNode> sNew = new Stack<TreeNode> ();
		List<Integer> level = new LinkedList<Integer> ();
		boolean order = true;
		s.push(root);
		while (!s.isEmpty()) {
			TreeNode node = s.pop();
			if (order) {
				if (node.left != null) sNew.push(node.left);
				if (node.right != null) sNew.push(node.right);
			} else {
				if (node.right != null) sNew.push(node.right);
				if (node.left != null) sNew.push(node.left);
			}
			level.add(node.val);
			
			if (s.isEmpty()) {
				result.add(level);
				level = new LinkedList<Integer> ();
				s = sNew;
				sNew = new Stack<TreeNode> ();
				order = !order;
			}
			
		}
		return result;
    }
}
