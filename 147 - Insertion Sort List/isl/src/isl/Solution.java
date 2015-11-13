package isl;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode insertionSortList(ListNode head) {
        if (head == null) return head;
        
        ListNode anchor = new ListNode (0);
        anchor.next = head;
        ListNode ptrHeadUnsorted = head.next;
        head.next = null;
        
        while (ptrHeadUnsorted != null) {
        	ListNode node = ptrHeadUnsorted;
        	ptrHeadUnsorted = ptrHeadUnsorted.next;
        	node.next = null;
        	
        	ListNode ptr = anchor;
        	while (ptr.next != null && ptr.next.val < node.val) {
        		ptr = ptr.next;
        	}
        	node.next = ptr.next;
        	ptr.next = node;
        }
        return anchor.next;
    }
}
