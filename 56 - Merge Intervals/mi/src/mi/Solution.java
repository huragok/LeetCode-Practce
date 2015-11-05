package mi;

import java.util.List;
import java.util.ArrayList;
import java.util.Comparator;
import java.util.Collections;

public class Solution {
	public class Interval {
		int start;
		int end;
		Interval() { start = 0; end = 0; }
		Interval(int s, int e) { start = s; end = e; }
	}
	
	public class IntervalComparator implements Comparator<Interval> {
		public int compare(Interval i1, Interval i2) {
			return i1.start - i2.start;
		}
	}
	
	public List<Interval> merge(List<Interval> intervals) {
		IntervalComparator comparator = new IntervalComparator();
        Collections.sort(intervals, comparator);
        
        int n = intervals.size();
        List<Interval> result = new ArrayList<Interval> ();
        if (n == 0) {
        	return result;
        }
        int left = intervals.get(0).start, right = intervals.get(0).end;
        for (int i = 1; i < n; i++) {
        	Interval itv = intervals.get(i);
        	if (itv.start <= right) { // merge
        		right = right > itv.end ? right : itv.end;
        	} else {
        		result.add(new Interval (left, right));
        		left = itv.start; right = itv.end;
        	}
        }
        result.add(new Interval (left, right));
        
        return result;
    }
}
