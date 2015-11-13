package llc2;

public class Solution {
	class ListNode {
		int val;
		ListNode next;
		ListNode(int x) {
			val = x;
			next = null;
		}
	}
	
	public ListNode detectCycle(ListNode head) {
		ListNode anchor = new ListNode (0);
		anchor.next = head;
		
		ListNode ptrFast = head;
		ListNode ptrSlow = anchor;
		
		int count = 0;
		
		while (ptrFast != null) {
			ptrFast = ptrFast.next;
			if (ptrFast == null) return null;
			ptrFast = ptrFast.next;
			
			ptrSlow = ptrSlow.next;
			count++;
			if (ptrFast == ptrSlow) { // The length of the circle is count + 1
				ListNode ptrFirst = anchor;
				for (int i = 0; i < count + 1; i++) {
					ptrFirst = ptrFirst.next;
				}
				ListNode ptrSecond = anchor;
				while (ptrFirst != ptrSecond) {
					ptrFirst = ptrFirst.next;
					ptrSecond = ptrSecond.next;
				}
				return ptrFirst;
				
			}
		}
		
		return null;
    }
}
