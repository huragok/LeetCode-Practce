package mdbt;

import java.util.Queue;
import java.util.LinkedList;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public int minDepth(TreeNode root) {
        if (root == null) return 0;
        Queue<TreeNode> level = new LinkedList<TreeNode> ();
        level.add(root);
        Queue<TreeNode> levelNew = new LinkedList<TreeNode> ();
        int depth = 1;
        while (!level.isEmpty()) {
        	TreeNode node = level.poll();
        	if (node.left == null && node.right == null) return depth;
        	if (node.left != null) levelNew.add(node.left);
        	if (node.right != null) levelNew.add(node.right);
        	
        	if (level.isEmpty()) {
        		level = levelNew;
        		levelNew = new LinkedList<TreeNode> ();
        		depth++;
        	}
        }
        
        return 0;
    }
}
