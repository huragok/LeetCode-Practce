package pl;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
    public ListNode partition(ListNode head, int x) {
        ListNode anchor = new ListNode(0);
        anchor.next = head;
        ListNode ptrTailLeft = anchor;// Tail of the list that is smaller than x
        ListNode anchor2 = new ListNode(0);
        anchor2.next = head;
        ListNode ptr = anchor2;

        while (ptr.next != null) {
        	if (ptr.next.val < x) {
        		ListNode tmp = ptr.next.next;
        		ptrTailLeft.next = ptr.next;
        		ptrTailLeft = ptrTailLeft.next;
        		ptr.next = tmp;
        	} else {
        		ptr = ptr.next;
        	}
        }
        ptrTailLeft.next = anchor2.next;
        return anchor.next;
        
    }
}