package mtsl;

public class Solution {
	
	public static class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode anchor = new ListNode(-1);
        ListNode ptr = anchor;
        
        ListNode ptr1 = l1;
        ListNode ptr2 = l2;
        
        while (ptr1 != null || ptr2 != null) {
        	if (ptr1 != null && ptr2 != null) {
        		if (ptr1.val < ptr2.val) {
        			ptr.next = ptr1;
        			ptr1 = ptr1.next;
        		} else {
        			ptr.next = ptr2;
        			ptr2 = ptr2.next;
        		}
        	} else if (ptr1 != null) {
        		ptr.next = ptr1;
        		ptr1 = ptr1.next;
        	} else {
        		ptr.next = ptr2;
    			ptr2 = ptr2.next;
        	}
        	ptr = ptr.next;
        }
        
        return anchor.next;
    }
}
