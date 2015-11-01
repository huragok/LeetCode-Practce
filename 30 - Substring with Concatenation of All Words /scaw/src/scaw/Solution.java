package scaw;

import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.ArrayList;
import java.util.List;

public class Solution {
	public List<Integer> findSubstring(String s, String[] words) {
        if (words.length == 0) {
        	return Arrays.asList();
        }
        int step = words[0].length();
        int len = s.length();
        int n = words.length;
        
        Map<String, Integer> count = new HashMap<String, Integer>(words.length);
        for (String word: words) {
        	count.put(word, 0);
        }
        for (String word: words) {
        	count.put(word, count.get(word) + 1);
        }
        
        List<String> indicator = new ArrayList<String> (len - step + 1);
        for (int j = 0; j < len - step + 1; j++){
        	String word = s.substring(j, j + step);
        	if (count.containsKey(word)) {
        		indicator.add(word);
        	} else {
        		indicator.add("\u0000");
        	}
        }
        
        List<Integer> result = new ArrayList<Integer> ();
        for (int start = 0; start < len - n * step + 1; start++) {
        	Map<String, Integer> countTmp = new HashMap<String, Integer> ();
        	for (int k = 0; k < n; k++) {
        		String word = indicator.get(start + k * step);
        		if (word != "\u0000") {
        			if (countTmp.containsKey(word)) {
        				countTmp.put(word, countTmp.get(word) + 1);
        			} else {
        				countTmp.put(word, 1);
        			}
        		}
        	}
        	
        	boolean flag = true;
        	for (String w: count.keySet()) {
        		if (!countTmp.containsKey(w) || countTmp.get(w) != count.get(w)) {
        			flag = false;
        			break;
        		}
        	}
        	
        	if (flag) {
        		result.add(start);
        	}
        }
        return result;
    }
	
	public static void main(String [] args) {
		String s = "wordgoodgoodgoodbestword";
		String [] words = {"word","good","best","good"};
		System.out.println(new Solution().findSubstring(s, words));
	}
}
