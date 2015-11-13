package llc;

public class Solution {
	class ListNode {
		int val;
		ListNode next;
		ListNode(int x) {
			val = x;
			next = null;
		}
	}
	
	public boolean hasCycle(ListNode head) {
		ListNode anchor = new ListNode(0);
		anchor.next = head;
		
		ListNode ptrFast = head;
		ListNode ptrSlow = anchor;
		
		while (ptrFast != null) {
			ptrFast = ptrFast.next;
			if (ptrFast == null) return false;
			ptrFast = ptrFast.next;
			
			ptrSlow = ptrSlow.next;
			
			if (ptrFast == ptrSlow) return true;
		}
        
		return false;
    }
}
