package mpl;
import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class Solution {
	class Point {
		int x;
		int y;
		Point() { x = 0; y = 0; }
		Point(int a, int b) { x = a; y = b; }
	}
	
	public int maxPoints(Point[] points) {
        int n = points.length;
        if (n == 0) return 0;
        Map<List<Integer>, Integer> count = new HashMap<List<Integer>, Integer> (); // Count by slope
        int maxCount = 0;
        List<Integer> slopeDup = new ArrayList<Integer> (2); slopeDup.add(0); slopeDup.add(0);
        for (int i = 0; i < n - 1; i++) {
        	count.clear();
        	for (int j = i + 1; j < n; j++) {
        		List<Integer> slope = getSlope(points[i], points[j]);
        		if (count.containsKey(slope)) count.put(slope, count.get(slope) + 1);
        		else count.put(slope, 1);
        	}
        	
        	if (count.containsKey(slopeDup)) {
        		int countDup = count.get(slopeDup);
        		for (List<Integer> s: count.keySet()) {
        			if (s.get(0) != 0 || s.get(1) != 0) {
        				count.put(s, count.get(s) + countDup);
        			}
        		}
        	}
        	
        	for (int c: count.values()) {
        		if (c > maxCount) maxCount = c;
        	}
        }
        return maxCount + 1;
    }
	
	private List<Integer> getSlope(Point p1, Point p2) {
		List<Integer> result = new ArrayList<Integer> ();
		if (p1.x == p2.x && p1.y == p2.y) {
			result.add(0); result.add(0);
		} else if (p1. x == p2.x){
			result.add(0); result.add(1);
		} else if (p1.y == p2.y) {
			result.add(1); result.add(0);
		} else {
			int offsetX = p2.x - p1.x;
			int offsetY = p2.y - p1.y;
			
			int gcd = getGCD(offsetX, offsetY);
			if (offsetX < 0) {
				offsetX = -offsetX;
				offsetY = -offsetY;
			}
			if (gcd == 0) {
				result.add(1); result.add(0);
			} else {
				result.add(offsetX / gcd); result.add(offsetY / gcd);
			}
		}
		return result;
	}
	
	private int getGCD(int a, int b) {
		if (a < 0) a = -a;
		if (b < 0) b = -b;
		
		while (a % b != 0) {
			a %= b;
			int tmp = a;
			a = b;
			b = tmp;
		}
		return b;
	}
}
