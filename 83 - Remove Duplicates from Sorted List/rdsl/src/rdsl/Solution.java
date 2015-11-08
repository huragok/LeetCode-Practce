package rdsl;

public class Solution {
	public class ListNode {
		int val;
		ListNode next;
		ListNode(int x) { val = x; }
	}
	
	public ListNode deleteDuplicates(ListNode head) {
        if (head == null) return head;
        
        ListNode anchor = new ListNode(0);
        anchor.next = head;
        ListNode ptrTailUnique = anchor;
        ListNode ptr = head;
        int valLast = head.val - 1;
        
        while (ptr != null) {
        	if (ptr.val != valLast) {
        		valLast = ptr.val;
        		ptrTailUnique.next = ptr;
        		ptrTailUnique = ptrTailUnique.next;
        	}
        	ptr = ptr.next;
        }
        ptrTailUnique.next = null;
        return anchor.next;
    }
}
