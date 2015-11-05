package ii;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	public static class Interval {
		int start;
		int end;
		Interval() { start = 0; end = 0; }
		Interval(int s, int e) { start = s; end = e; }
	}
	
	public List<Interval> insert(List<Interval> intervals, Interval newInterval) {

        int idx = index(intervals, newInterval);
        intervals.add(idx, newInterval);
        System.out.println(idx);
        if (idx >= 1) {
        	if (intervals.get(idx - 1).end >= intervals.get(idx).start) {
        		System.out.println("fuck");
        		int left = intervals.get(idx - 1).start;
        		int right = intervals.get(idx - 1).end > intervals.get(idx).end ? intervals.get(idx - 1).end : intervals.get(idx).end;
        		intervals.remove(idx);
        		intervals.remove(idx - 1);
        		intervals.add(idx - 1, new Interval(left, right));
        		idx--;
        	}
        }
        mergeSince(intervals, idx);

        return intervals;
    }
	
	// Find the place to insert the interval according to the start value
	private int index(List<Interval> intervals, Interval newInterval) {
		int n = intervals.size();
		if (n == 0) {
			return 0;
		}
		int left = 0, right = n - 1;
		if (intervals.get(left).start > newInterval.start) { // Insert at the beginnning
			return 0;
		} else if (intervals.get(right).start <= newInterval.start) {
			return n;
		} else {
			while(right - left > 1) { // bisect search
				int mid = (left + right) / 2;
				if (intervals.get(mid).start <= newInterval.start) {
					left = mid;
				} else {
					right = mid;
				}
			}
			return left + 1;
		}
	}
	
	private void mergeSince(List<Interval> intervals, int idx) {
		int left = intervals.get(idx).start;
		int right = intervals.get(idx).end;
		intervals.remove(idx);
		
		int n = intervals.size();
		int i = idx;
		while (i < n) {
			if (intervals.get(i).start > right) {
				break;
			} else {
				
				Interval intv = intervals.get(i);
				right = intv.end > right ? intv.end : right;
				intervals.remove(i);
				n--;
			}
		}
		intervals.add(i, new Interval(left, right));
	}
	
	
	
	public static void main(String [] args) {
		List<Interval> intervals = new ArrayList<Interval> ();
		intervals.add(new Interval(1, 5));
		Interval newInterval = new Interval (2, 3);
		List<Interval> intervalsNew = new Solution().insert(intervals, newInterval);
		for (int i = 0; i < intervalsNew.size(); i++) {
			System.out.println(Integer.toString(intervals.get(i).start) + ", " + Integer.toString(intervals.get(i).end));
		}
		
	}
}
