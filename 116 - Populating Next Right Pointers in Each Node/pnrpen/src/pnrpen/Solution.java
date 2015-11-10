package pnrpen;

public class Solution {
	public class TreeLinkNode {
		int val;
		TreeLinkNode left, right, next;
		TreeLinkNode(int x) { val = x; }
	}
	
	public void connect(TreeLinkNode root) {
		if (root == null || root.left == null) return;
        
        TreeLinkNode ptrUp = root;
        TreeLinkNode ptrDown = root.left;
        
        while (root.left != null) {
        	while (ptrUp != null) {
        		if (ptrUp.left == ptrDown) {
        			ptrDown.next = ptrUp.right;
        			ptrUp = ptrUp.next;
        		} else {
        			ptrDown.next = ptrUp.left;
        		}
        		ptrDown = ptrDown.next;
        	}
        	ptrUp = root.left;
        	root = root.left;
        	ptrDown = root.left;
        }
    }
}
