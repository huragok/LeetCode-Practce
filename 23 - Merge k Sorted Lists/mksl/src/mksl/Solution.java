package mksl;

import java.util.PriorityQueue;
import java.util.Comparator;

public class Solution {
	
    public ListNode mergeKLists(ListNode[] lists) {
    	Comparator<ListNode> comparator = new ListNodeComparator();
    	int n = lists.length;
    	if (n == 0) {
    		return null;
    	}
        PriorityQueue<ListNode> q = new PriorityQueue<ListNode>(n, comparator);
        
        for (ListNode l: lists) {
        	if (l != null) {
        		q.add(l);
        	}
        }
        
        ListNode anchor = new ListNode(0);
        ListNode ptr = anchor;
        
        while (!q.isEmpty()) {
        	ListNode l = q.poll();
        	ptr.next = l;
        	ptr = ptr.next;
        	
        	if (l.next != null) {
        		q.add(l.next);
        	}
        }
        
        return anchor.next;
    }
}
