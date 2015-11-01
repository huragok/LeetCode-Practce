package snp;

public class Solution {
	public static class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode swapPairs(ListNode head) {
        ListNode anchor = new ListNode(0);
        ListNode ptr = anchor;
        
        ListNode left = head;
        if (left == null) {
        	return head;
        }
        ListNode right = head.next;
        if (right == null) {
        	return head;
        }
        
        while (right != null) {
        	ListNode leftNew = right.next;
        	ptr.next = right; ptr = ptr.next;
        	ptr.next = left; ptr = ptr.next;
        	
        	left = leftNew;
        	if (left == null) {
        		break;
        	}
        	right = left.next;
        }
        
        if (left != null) {
        	ptr.next = left; ptr = ptr.next;
        }
        ptr.next = null;
        
        return anchor.next;
    }
}
