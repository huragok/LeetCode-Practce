package is;
import java.util.Map;
import java.util.HashMap;
public class Solution {
	public boolean isIsomorphic(String s, String t) {
		int n = s.length();
		if (n != t.length()) return false;
		
		Map<Character, Character> mapst = new HashMap<Character, Character> ();
		Map<Character, Character> mapts = new HashMap<Character, Character> ();
		for (int i = 0; i < n; i++) {
			char cs = s.charAt(i);
			char ct = t.charAt(i);
			
			if (mapst.containsKey(cs) && mapts.containsKey(ct)) {
				if (ct != mapst.get(cs) || cs != mapts.get(ct)) return false;
			} else if (!mapst.containsKey(cs) && !mapts.containsKey(ct)) {
				mapst.put(cs, ct); mapts.put(ct, cs);
			} else {
				return false;
			}
		}
		return true;
        
    }
}
