package wl;

import java.util.Set;
import java.util.HashSet;

public class Solution {
	public int ladderLength(String beginWord, String endWord, Set<String> wordList) {
			
        int n = wordList.size();
        int l = beginWord.length();
        
        char [] alphabet = new char [] {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        
        Set<String> wordsForward = new HashSet<String> (); wordsForward.add(beginWord);
        Set<String> wordsBackward = new HashSet<String> (); wordsBackward.add(endWord);
        Set<String> wordsToRemove;
        
        int count = 0;
        boolean found = false;
        while (!wordList.isEmpty() && count < n) {
        	wordsToRemove = new HashSet<String> ();
        	if (wordsForward.size() < wordsBackward.size()) {
        		for (String word: wordsForward) {
        			for (int i = 0; i < l; i++) {
        				char cTmp = word.charAt(i);
        				for (char c: alphabet) {
        					if (c != cTmp) {
        						String wordNew = new String (word.substring(0, i) + Character.toString(c) + word.substring(i + 1, l));
        						if (wordsBackward.contains(wordNew)) {
        							found = true;
        						} else if (wordList.contains(wordNew)){
        							wordsToRemove.add(wordNew);
        						}
        					}
        				}
        			}
        		}
        		
        		wordsForward = wordsToRemove;
        		wordList.removeAll(wordsToRemove);
        	} else {
        		for (String word: wordsBackward) {
        			for (int i = 0; i < l; i++) {
        				char cTmp = word.charAt(i);
        				for (char c: alphabet) {
        					if (c != cTmp) {
        						String wordNew = new String (word.substring(0, i) + Character.toString(c) + word.substring(i + 1, l));
        						if (wordsForward.contains(wordNew)) {
        							found = true;
        						} else if (wordList.contains(wordNew)){
        							wordsToRemove.add(wordNew);
        						}
        					}
        				}
        			}
        		}
        		
        		wordsBackward = wordsToRemove;
        		wordList.removeAll(wordsToRemove);
        	}
        	if (found) break;
        	count++;
        }
        if (count == n) {
        	return 0;
        } else {
        	return count + 2;
        }
    }
	
}
