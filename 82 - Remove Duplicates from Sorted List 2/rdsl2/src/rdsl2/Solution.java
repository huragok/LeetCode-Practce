package rdsl2;

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
        boolean duplicate = false;
        
        ListNode ptr = head;
        while (ptr != null) {
        	if (ptr.next == null || ptr.next.val != ptr.val) {
        		if (!duplicate) {
        			ptrTailUnique.next = ptr;
        			ptrTailUnique = ptrTailUnique.next;
        		} else {
        			duplicate = false;
        		}
        	} else {
        		duplicate = true;
        	}
        	ptr = ptr.next;
        }
        ptrTailUnique.next = null;
        return anchor.next;
        
    }
}
