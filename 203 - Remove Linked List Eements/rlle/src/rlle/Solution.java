package rlle;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode removeElements(ListNode head, int val) {
		ListNode anchor = new ListNode (0);
		anchor.next = head;
		
		ListNode curr = anchor;
		
		while (curr.next != null) {
			if (curr.next.val == val) {
				curr.next = curr.next.next;
			} else {
				curr = curr.next;
			}
		}
		return anchor.next;
    }
}
