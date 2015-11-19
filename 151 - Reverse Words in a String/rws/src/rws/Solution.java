package rws;

public class Solution {
	public String reverseWords(String s) {
        String [] words = s.split("\\s+");
		String result = "";
		for (String word: words) {
			result = word + " " + result;
		}
		return result.trim();
    }
}
