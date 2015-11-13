package rl;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public void reorderList(ListNode head) {
        ListNode mid = halve(head);
        ListNode midReversed = reverse(mid);
        merge(head, midReversed);
    }
	
	private ListNode halve(ListNode head) {
		ListNode anchor = new ListNode (0);
        anchor.next = head;
        
        ListNode ptrSlow = anchor, ptrFast = anchor;
        while (ptrFast != null) {
        	ptrFast = ptrFast.next;
        	if (ptrFast == null) break;
        	ptrFast = ptrFast.next;
        	
        	ptrSlow = ptrSlow.next;
        }
        ListNode result = ptrSlow.next;
        ptrSlow.next = null;
        return result;
	}
	
	private ListNode reverse(ListNode head) {
		if (head == null) return null;
		

		
		ListNode headReversed = head;
		ListNode headOrdered = head.next;
		head.next = null;
		while (headOrdered != null) {
			ListNode tmp = headOrdered.next;
			headOrdered.next = headReversed;
			headReversed = headOrdered;
			headOrdered = tmp;
		}
		return headReversed;
	}
	
	private void merge(ListNode head1, ListNode head2) {
		ListNode anchor = new ListNode(0);
		ListNode ptr = anchor;
		
		ListNode ptr1 = head1;
		ListNode ptr2 = head2;
		
		while (ptr1 != null || ptr2 != null) {
			if (ptr1 != null) {
				ptr.next = ptr1;
				ptr = ptr.next;
				ptr1 = ptr1.next;
			}
			
			if (ptr2 != null) {
				ptr.next = ptr2;
				ptr = ptr.next;
				ptr2 = ptr2.next;
			}
		}
		ptr.next = null;
	}
}
