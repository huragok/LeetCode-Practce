package atn;

public class Solution {
	
	protected class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carryOn = 0;
        ListNode ptr1 = l1;
        ListNode ptr2 = l2;
        
        ListNode anchor = new ListNode(-1);
        ListNode ptr = anchor;
        
        while (ptr1 != null || ptr2 != null) {
        	int s = carryOn;
        	if (ptr1 != null) {
        		s += ptr1.val;
        		ptr1 = ptr1.next;
        	} 
        	if (ptr2 != null) {
        		s += ptr2.val;
        		ptr2 = ptr2.next;
        	} 
        	if (s > 9) {
        		s = s - 10;
        		carryOn = 1;
        	} else {
        		carryOn = 0;
        	}
        	ptr.next = new ListNode(s);
        	ptr = ptr.next;
        }
        if (carryOn > 0) {
        	ptr.next = new ListNode(1);
        }
        
        return anchor.next;
    }

}
