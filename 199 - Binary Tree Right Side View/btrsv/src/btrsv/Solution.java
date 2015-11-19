package btrsv;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public List<Integer> rightSideView(TreeNode root) {
		List<Integer> result = new ArrayList<Integer> ();
		if (root == null) return result;
		
		List<TreeNode> level = new ArrayList<TreeNode> ();
		level.add(root);
		
		while (!level.isEmpty()) {
			List<TreeNode> levelNew = new ArrayList<TreeNode> ();
			for (TreeNode node: level) {
				if (node.left != null) levelNew.add(node.left);
				if (node.right != null) levelNew.add(node.right);
			}
			result.add(level.get(level.size() - 1).val);
			level = levelNew;
		}
		return result;
    }
}
