package ss;

import java.util.Map;
import java.util.HashMap;

public class Solution {
	private static int [] prime = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101};
	private static char [] alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
	private static Map<Character, Integer> map;
	static {
		map = new HashMap<Character, Integer> ();
		for (int i = 0; i < 26; i++) {
			map.put(alphabet[i], prime[i]);
		}
	}
	private int [][] hashVal1;
	private int [][] hashVal2;
	private String s1, s2;
	
	public boolean isScramble(String s1, String s2) {
		this.s1 = s1;
		this.s2 = s2;
        int m = s1.length(), n = s2.length();
        if (m != n) return false;
        
        hashVal1 = new int [n][n + 1]; // The hash value of the substirng s1.substring(i, j)
        hashVal2 = new int [n][n + 1];
        for (int i = 0; i < n; i++) {
        	hashVal1[i][i] = 1;
        	hashVal2[i][i] = 1;
        	for (int j = i + 1; j < n + 1; j++) {
        		hashVal1[i][j] = hashVal1[i][j - 1] * map.get(s1.charAt(j - 1));
        		hashVal2[i][j] = hashVal2[i][j - 1] * map.get(s2.charAt(j - 1));
        	}
        }
        
        return isScramble(0, n, 0, n);
    }
	
	private boolean isScramble(int i1, int j1, int i2, int j2) {
		if (j1 - i1 != j2 - i2 || hashVal1[i1][j1] != hashVal2[i2][j2]) {
			return false;
		} else if (s1.substring(i1, j1).equals(s2.substring(i2, j2))) {
			return true;
		} else {
			for (int l = 1; l < j1 - i1; l++) { // The length of the left substing in s1.substring(i1, j1)
				if (isScramble(i1, i1 + l, i2, i2 + l) && isScramble(i1 + l, j1, i2 + l, j2)) return true;
				if (isScramble(i1, i1 + l, i2 + (j1 - i1 - l), j2) && isScramble(i1 + l, j1, i2, i2 + (j1 - i1 - l))) return true;
			}
			return false;
		}
	}
	
	public static void main(String [] args) {
		String s1 = "rgtae";
		String s2 = "great";
		System.out.println(new Solution().isScramble(s1, s2));
	}
}
