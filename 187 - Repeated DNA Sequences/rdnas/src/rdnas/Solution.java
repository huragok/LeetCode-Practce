package rdnas;

import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class Solution {
	
	public List<String> findRepeatedDnaSequences(String s) {
		int n = s.length();
		List<String> result = new ArrayList<String> ();
		Map<String, Integer> count = new HashMap<String, Integer> ();
		for (int i = 10; i <= n; i++) {
			String sub = s.substring(i - 10, i);
			if (count.containsKey(sub)) {
				count.put(sub, count.get(sub) + 1);
			} else {
				count.put(sub, 1);
			}
		}
		
		for (String sub: count.keySet()) {
			if (count.get(sub) > 1) {
				result.add(sub);
			}
		}
		return result;
    }
	
	
	public static void main(String [] args) {
		String s = "AAAAAAAAAAA";
		System.out.println(new Solution().findRepeatedDnaSequences(s));
	}
}
