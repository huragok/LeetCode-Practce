package lcpn;

import java.util.*;

public class Solution {
	private static Map<Character, List<Character>> map = new HashMap<Character,List<Character>> (8);
	static {
    	map.put('2', Arrays.asList('a', 'b', 'c'));
    	map.put('3', Arrays.asList('d', 'e', 'f'));
    	map.put('4', Arrays.asList('g', 'h', 'i'));
    	map.put('5', Arrays.asList('j', 'k', 'l'));
    	map.put('6', Arrays.asList('m', 'n', 'o'));
    	map.put('7', Arrays.asList('p', 'q', 'r', 's'));
    	map.put('8', Arrays.asList('t', 'u', 'v'));
    	map.put('9', Arrays.asList('w', 'x', 'y', 'z'));
	}
	
    public List<String> letterCombinations(String digits) {
    	List<String> comb = new ArrayList<String> ();
    	
    	return letterCombinationsSub(digits, comb);
    }
    
    private List<String> letterCombinationsSub(String digitsSub, List<String> comb)  {
    	if (digitsSub.length() == 0) {
    		return comb;
    	} else {
    		List <String> combSub = new ArrayList<String> ();
    		if (comb.size() == 0) {
    			for (char c: map.get(digitsSub.charAt(0))) {
    				combSub.add(String.valueOf(c));
    			}
    		} else {
    			for (String s: comb) {
        			for (char c: map.get(digitsSub.charAt(0))) {
        				combSub.add(s + c);
        			}
        		}
    		}

    		return letterCombinationsSub(digitsSub.substring(1), combSub);
    	}
    }
    
    public static void main(String [] args) {
    	String digits = "23";
    	
    	List<String> result = new Solution().letterCombinations(digits);
    	System.out.println(result);
    }
}
