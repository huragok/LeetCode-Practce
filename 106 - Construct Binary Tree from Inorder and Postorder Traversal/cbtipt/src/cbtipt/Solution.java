package cbtipt;

import java.util.Map;
import java.util.HashMap;

public class Solution {
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	Map<Integer, Integer> mapInorder;
	
	public TreeNode buildTree(int[] inorder, int[] postorder) {
        int n = inorder.length;
        mapInorder = new HashMap<Integer, Integer> ();
        for (int i = 0; i < n; i++) mapInorder.put(inorder[i], i);
        
        return buildTree(inorder, postorder, 0, n, 0, n);
    }
	
	private TreeNode buildTree(int[] inorder, int[] postorder, int li, int ui, int lp, int up) {
		if (ui <= li) return null;
		TreeNode root = new TreeNode(postorder[up - 1]);
		int idxRoot = mapInorder.get(root.val);
		int lenRightTree = ui - idxRoot;
		TreeNode rootRight = buildTree(inorder, postorder, idxRoot + 1, ui, up - lenRightTree - 1, up - 1);
		TreeNode rootLeft = buildTree(inorder, postorder, li, idxRoot, lp, up - lenRightTree - 1);
		root.left = rootLeft; root.right = rootRight;
		return root;
	}
}
