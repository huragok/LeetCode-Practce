package it;

import java.util.Map;
import java.util.HashMap;

class TrieNode {
    // Initialize your data structure here.
    public char val;
    public boolean isWord;
    public TrieNode [] children;
	
	public TrieNode() {
		isWord = false;
		children = new TrieNode [26];
    }
}

public class Trie {
	private TrieNode root;

    public Trie() {
        root = new TrieNode();
    }

    // Inserts a word into the trie.
    public void insert(String word) {
    	TrieNode curr = root;
        for (int i = 0; i < word.length(); i++) {
        	char c = word.charAt(i);
        	int idx = c - 'a';
        	if (curr.children[idx] == null) {
        		TrieNode child = new TrieNode();
        		child.val = c;
        		curr.children[idx] = child;
        	}
        	curr = curr.children[idx];
        }
        curr.isWord = true;
    }

    // Returns if the word is in the trie.
    public boolean search(String word) {
        TrieNode curr = root;
        for (int i = 0; i < word.length(); i++) {
        	char c = word.charAt(i);
        	int idx = c - 'a';
        	if (curr.children[idx] == null) {
        		return false;
        	} else {
        		curr = curr.children[idx];
        	}
        }
        return curr.isWord;
    }

    // Returns if there is any word in the trie
    // that starts with the given prefix.
    public boolean startsWith(String prefix) {
    	TrieNode curr = root;
        for (int i = 0; i < prefix.length(); i++) {
        	char c = prefix.charAt(i);
        	int idx = c - 'a';
        	if (curr.children[idx] == null) {
        		return false;
        	} else {
        		curr = curr.children[idx];
        	}
        }
        return true;
    }
}
