package rll;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode reverseList(ListNode head) {
		if (head == null) return null;
        
        ListNode headReversed = head;
        ListNode headOrdered = head.next;
        head.next = null;
        
        while (headOrdered != null) {
        	ListNode headOrderedNew = headOrdered.next;
        	headOrdered.next = headReversed;
        	headReversed = headOrdered;
        	headOrdered = headOrderedNew;
        }
        return headReversed;
    }
}
