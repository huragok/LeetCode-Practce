package wb2;

import java.util.HashSet;
import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.Map;
import java.util.HashMap;

public class Solution {
	private Map<Integer, List<String>> sentences;
	private Set<String> wordDict;
	private int n;
	private String s;
	public List<String> wordBreak(String s, Set<String> wordDict) {
        int n = s.length();
        
        sentences = new HashMap<Integer, List<String>> (n + 1); // sentences[i] contains all the sentences formed by s[i : n]
        List<String> sentencesEmpty = new ArrayList<String> (); sentencesEmpty.add("");
        sentences.put(n, sentencesEmpty);
        this.wordDict = wordDict;
        this.n = n;
        this.s = s;
        // Start the backtracking
        
        dfs(0);
        
        // Remove the left first space in all the resulting sentenes;
        List<String> result = new ArrayList<String> (sentences.get(0).size());
        for (String sentence: sentences.get(0)) {
        	result.add(sentence.trim());
        }
        
        return result;
	}
	
	private List<String> dfs(int i) {
		if (sentences.containsKey(i)) return sentences.get(i);
		
		List<String> sentencesPartial = new ArrayList<String> ();
		for (int l = 1; l <= n - i; l++) {
			if (wordDict.contains(s.substring(i, i + l))) {
				for (String sentence: dfs(i + l)) {
					sentencesPartial.add(s.substring(i, i + l) + " " + sentence);
				}
			}
		}
		sentences.put(i, sentencesPartial);
		return sentencesPartial;
	}
	
	public static void main(String [] args) {
		String s = "catsanddog";
		Set<String> wordDict = new HashSet<String> ();
		for (String word: new String [] {"cat", "cats", "and", "sand", "dog"}) {
			wordDict.add(word);
		}
		System.out.println(new Solution().wordBreak(s, wordDict));
	}
}
