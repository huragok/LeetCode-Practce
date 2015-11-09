package cslbst;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public class TreeNode {
		int val;
		TreeNode left;
		TreeNode right;
		TreeNode(int x) { val = x; }
	}
	
	private ListNode ptr;
	public TreeNode sortedListToBST(ListNode head) {
        if (head == null) return null;
        
        
        // Detect the length of the linked list
        ptr = head;
        int n = 0;
        while (ptr != null) {
        	ptr = ptr.next;
        	n++;
        }
        
        ptr = head;
        return sortedListToBST(n);
    }
	
	private TreeNode sortedListToBST(int l) {
        if (l == 0) return null;
        
        int lLeft= (l - 1) / 2;
        int lRight = l - 1 - lLeft;
        
        TreeNode rootLeft = sortedListToBST(lLeft);
        TreeNode root = new TreeNode(ptr.val);
        ptr = ptr.next;
        TreeNode rootRight = sortedListToBST(lRight);
        
        root.left = rootLeft; root.right = rootRight;
        return root;
    }
}
