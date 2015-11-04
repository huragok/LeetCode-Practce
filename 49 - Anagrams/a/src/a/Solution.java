package a;

import java.util.Collections;
import java.util.List;
import java.util.ArrayList;
import java.util.Map;
import java.util.HashMap;

public class Solution {
	static final Map<Character, Integer> map;
	static {
		map = new HashMap<Character, Integer> (26);
		map.put('a', 2); map.put('b', 3); map.put('c', 5);map.put('d', 7);
		map.put('e', 11); map.put('f', 13);map.put('g', 17); map.put('h', 19);
		map.put('i', 23); map.put('j', 29);map.put('k', 31); map.put('l', 37);
		map.put('m', 41); map.put('n', 43);map.put('o', 47); map.put('p', 53);
		map.put('q', 59); map.put('r', 61);map.put('s', 67); map.put('t', 71);
		map.put('u', 73); map.put('v', 79);map.put('w', 83); map.put('x', 89);
		map.put('y', 97); map.put('z', 101);
		
	}
	
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<Integer, List<String>> groups = new HashMap<Integer, List<String>> ();
        for (String str: strs) {
        	int key = hash(str);
        	if (groups.containsKey(key)) {
        		groups.get(key).add(str);
        	} else {
        		List<String> group = new ArrayList<String> ();
        		group.add(str);
        		groups.put(key, group);
        	}
        }
        
        List<List<String>> result = new ArrayList<List<String>> (groups.size());
        for (List<String> group: groups.values()) {
        	Collections.sort(group);
        }
        result.addAll(groups.values());
        return result;
    }
    
    private int hash(String str) {
    	int result = 1;
    	for (int i = 0; i < str.length(); i++) {
    		result *= map.get(str.charAt(i));
    	}
    	return result;
    }
    
    public static void main(String [] args) {
    	String [] strs = {"eat", "tea", "tan", "ate", "nat", "bat"};
    	System.out.println(new Solution().groupAnagrams(strs));
    }
}
