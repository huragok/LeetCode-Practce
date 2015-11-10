package wl2;

import java.util.List;
import java.util.ArrayList;
import java.util.Set;
import java.util.HashSet;

public class Solution {
	public List<List<String>> findLadders(String beginWord, String endWord, Set<String> wordList) {
		
		List<List<String>> result = new ArrayList<List<String>> ();
		if (beginWord.equals(endWord)) {
			List<String> ladder = new ArrayList<String> ();
			ladder.add(beginWord);
			result.add(ladder);
			return result;
		}
		
        char [] alpha = new char [] {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
        Set<String> wordToRemove;
        
        Set<String> wordsForward = new HashSet<String> (); wordsForward.add(beginWord);
        Set<String> wordsBackward = new HashSet<String> (); wordsBackward.add(endWord);
        Set<String> wordsNew;
        
        List<List<String>> pathsForward = new ArrayList<List<String>> ();
        List<List<String>> pathsBackward = new ArrayList<List<String>> ();
        List<List<String>> pathsNew;
        
        List<String> path = new ArrayList<String> (); path.add(beginWord); pathsForward.add(path);
        path = new ArrayList<String> (); path.add(endWord); pathsBackward.add(path);
        
        int l = beginWord.length();
        int n = wordList.size();
        
        boolean found = false;
        int count = 0;
        
        while (!wordList.isEmpty() && count < n) {
        	wordToRemove = new HashSet<String> ();
        	wordsNew = new HashSet<String> ();
        	pathsNew = new ArrayList<List<String>> ();
        	if (wordsForward.size() < wordsBackward.size()) {
            	for (String word: wordsForward) { // Each word in the current set
            		for (int i = 0; i < l; i++) { // each position in the word
            			char cTmp = word.charAt(i);
            			for (char letter: alpha) { // The letter used to replace
            				if (letter != cTmp) {
            					String wordNew = word.substring(0, i) + Character.toString(letter) + word.substring(i + 1, l);
            					
            					if (wordsBackward.contains(wordNew)) { // A path has been found
            						found = true;
            						for (List<String> pathForward: pathsForward) {
            							if (pathForward.get(pathForward.size() - 1).equals(word)) {
            								for (List<String> pathBackward: pathsBackward) {
            									if (pathBackward.get(0).equals(wordNew)) {
            										List<String> ladder = new ArrayList<String> (pathForward);
            										ladder.addAll(pathBackward);
            										result.add(ladder);
            									}
            								}
            							}
            						}
            						
            					} else if (wordList.contains(wordNew)) { //
            						wordToRemove.add(wordNew);
            						wordsNew.add(wordNew);
            						for (List<String> pathForward: pathsForward) {
            							if (pathForward.get(pathForward.size() - 1).equals(word)) {
            								List<String> pathNew = new ArrayList<String> (pathForward);
            								pathNew.add(wordNew);
            								pathsNew.add(pathNew);
            							}
            						}
            					}
            				
            				}
            			}
            		}
            	}
            	
            	if (!found) {
            		wordList.removeAll(wordToRemove);
            		wordsForward = wordsNew;
            		pathsForward = pathsNew;
            	} else {
            		break;
            	}
            } else {
            	for (String word: wordsBackward) { // Each word in the current set
            		for (int i = 0; i < l; i++) { // each position in the word
            			char cTmp = word.charAt(i);
            			for (char letter: alpha) { // The letter used to replace
            				if (letter != cTmp) {
            					String wordNew = word.substring(0, i) + Character.toString(letter) + word.substring(i + 1, l);
            					
            					if (wordsForward.contains(wordNew)) { // A path has been found
            						found = true;
            						for (List<String> pathBackward: pathsBackward) {
            							if (pathBackward.get(0).equals(word)) {
            								for (List<String> pathForward: pathsForward) {
            									if (pathForward.get(pathForward.size() - 1).equals(wordNew)) {
            										List<String> ladder = new ArrayList<String> (pathForward);
            										ladder.addAll(pathBackward);
            										result.add(ladder);
            									}
            								}
            							}
            						}
            						
            					} else if (wordList.contains(wordNew)) { //
            						wordToRemove.add(wordNew);
            						wordsNew.add(wordNew);
            						for (List<String> pathBackward: pathsBackward) {
            							if (pathBackward.get(0).equals(word)) {
            								List<String> pathNew = new ArrayList<String> (pathBackward);
            								pathNew.add(0, wordNew);
            								pathsNew.add(pathNew);
            							}
            						}
            					}
            				
            				}
            			}
            		}
            	}
            	
            	if (!found) {
            		wordList.removeAll(wordToRemove);
            		wordsBackward = wordsNew;
            		pathsBackward = pathsNew;
            	} else {
            		break;
            	}
            }
        	count++;
        }
        return result;
    }
}
