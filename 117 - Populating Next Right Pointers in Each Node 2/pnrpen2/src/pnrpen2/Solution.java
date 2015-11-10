package pnrpen2;

public class Solution {
	public static class TreeLinkNode {
		int val;
		TreeLinkNode left, right, next;
		TreeLinkNode(int x) { val = x; }
	}
	
	public void connect(TreeLinkNode root) {
        if (root == null) return;
        
        TreeLinkNode ptrUp = root;
        TreeLinkNode anchor = new TreeLinkNode(0);
        TreeLinkNode ptrDown = anchor;
        
        
        while (ptrUp != null) {
        	ptrDown.next = ptrUp.left;
        	if (ptrDown.next != null) ptrDown = ptrDown.next;
        	ptrDown.next = ptrUp.right;
        	if (ptrDown.next != null) ptrDown = ptrDown.next;
        	
        	ptrUp = ptrUp.next;
        	
        	if (ptrUp == null) {
        		ptrUp = anchor.next;
        		ptrDown = anchor;
        	}
        }
    }
	
	public static void main(String [] args) {
		TreeLinkNode root = new TreeLinkNode(1);
		TreeLinkNode node = new TreeLinkNode(2);
		root.left = node;
		new Solution().connect(root);
		System.out.println(root.next.val);
		System.out.println(node.next.val);
	}
}
