package ps2;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	private List<Integer> path = new ArrayList<Integer> ();
	private List<List<Integer>> result = new ArrayList<List<Integer>> ();
	
	public List<List<Integer>> pathSum(TreeNode root, int sum) {
        if (root != null) {
        	path.add(root.val);
        	sum -= root.val;
        	if (root.left == null && root.right == null) {
        		if (sum == 0) result.add(new ArrayList<Integer> (path));
        	} else {
        		if (root.left != null) pathSum(root.left, sum);
        		if (root.right != null) pathSum(root.right, sum);
        	}
        	sum += root.val;
        	path.remove(path.size() - 1);
        }
        return result;
    }
}
