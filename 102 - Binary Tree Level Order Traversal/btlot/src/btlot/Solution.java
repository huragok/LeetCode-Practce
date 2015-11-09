package btlot;

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
	
	public List<List<Integer>> levelOrder(TreeNode root) {
        
        List<List<Integer>> result = new LinkedList<List<Integer>> ();
        if (root == null) {
        	return result;
        }
        Queue<TreeNode> q = new LinkedList<TreeNode> ();
        q.add(root);
        int countLevel = 1;
        int countLevelNew = 0;
        List<Integer> level = new LinkedList<Integer> ();
        while (!q.isEmpty()) {

        	TreeNode node = q.poll();
        	countLevel--;
        	if (node.left != null) {
        		q.add(node.left);
        		countLevelNew++;
        	}
        	
        	if (node.right != null) {
        		q.add(node.right);
        		countLevelNew++;
        	}
        	level.add(node.val);
        	
        	if (countLevel == 0) {
        		result.add(level);
        		countLevel = countLevelNew;
        		countLevelNew = 0;
        		level = new LinkedList<Integer> ();
        	}
        	
        }
        return result;
    }	
}
