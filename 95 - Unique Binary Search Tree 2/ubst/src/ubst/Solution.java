package ubst;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	public List<TreeNode> generateTrees(int n) {
		List<List<List<TreeNode>>> trees = new ArrayList<List<List<TreeNode>>> (); // trees[i, d] contains all trees generated from i + 1 to i + d + 1 (exclusive)
		for (int i = 0; i <= n; i++) {
			trees.add(new ArrayList<List<TreeNode>> ());
			for (int d = 0; d <= n - i; d++) {
				trees.get(i).add(new ArrayList<TreeNode> ());
			}
		}
		
		for (int i = 0; i <= n; i++){
			trees.get(i).get(0).add(null);
		}
		
		for (int d = 1; d <= n; d++) {
			for (int i = 0; i <= n - d; i++) {
				for (int valRoot = i; valRoot < i + d; valRoot++) {
					for (TreeNode rootLeft: trees.get(i).get(valRoot - i)) {
						for (TreeNode rootRight: trees.get(valRoot + 1).get(i + d - valRoot - 1)) {
							TreeNode rootNew = new TreeNode(valRoot + 1);
							rootNew.left = rootLeft; rootNew.right = rootRight;
							trees.get(i).get(d).add(rootNew);
						}
					}
				}
			}
		}
		
		return trees.get(0).get(n);
    }
	
}
