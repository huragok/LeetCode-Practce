package cbtpit;

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
	
	public TreeNode buildTree(int[] preorder, int[] inorder) {
		int n = preorder.length;
		mapInorder = new HashMap<Integer, Integer> ();
        for (int i = 0; i < n; i++) mapInorder.put(inorder[i], i);
        
        return buildTree(preorder, inorder, 0, n, 0, n);
    }
	
	private TreeNode buildTree(int[] preorder, int[] inorder, int lp, int up, int li, int ui) {
		if (up <= lp) return null;
		
		TreeNode root = new TreeNode(preorder[lp]);
		int idxRoot = mapInorder.get(root.val);
		int lenLeftTree = idxRoot - li;
		TreeNode rootLeft = buildTree(preorder, inorder, lp + 1, lp + 1 + lenLeftTree, li, idxRoot);
		TreeNode rootRight = buildTree(preorder, inorder, lp + 1 + lenLeftTree, up, idxRoot + 1, ui);
		root.left = rootLeft; root.right = rootRight;
		return root;
	}
	
}
