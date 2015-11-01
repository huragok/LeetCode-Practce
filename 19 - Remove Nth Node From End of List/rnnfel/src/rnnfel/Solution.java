package rnnfel;


public class Solution {
	public static class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
    public ListNode removeNthFromEnd(ListNode head, int n) {
        int count = 0;
        ListNode ptrRight = head;
        ListNode anchor = new  ListNode(-1);
        anchor.next = head;
        while (ptrRight != null && count < n) {
        	ptrRight = ptrRight.next;
        	count++;
        }
        if (count == n) {
        	ListNode ptrLeft = anchor;
        	while (ptrRight != null) {
        		ptrRight = ptrRight.next;
        		ptrLeft = ptrLeft.next;
        	}
        	
        	ptrLeft.next = ptrLeft.next.next;
        }
        return anchor.next;
    }
    
    
}