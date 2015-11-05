package ed;

public class Solution {
	public int minDistance(String word1, String word2) {
		int m = word1.length();
        int n = word2.length();
        
        int [] dist = new int [n + 1];
        for (int j = 0; j < n + 1; j++) {
        	dist[j] = j;
        }
        
        for (int i = 1; i < m + 1; i++) {
        	int [] distNew = new int [n + 1];
        	distNew[0] = i;
        	for (int j = 1; j < n + 1; j++) {
        		int d = dist[j - 1] + (word1.charAt(i - 1) == word2.charAt(j - 1) ? 0 : 1);
        		d = d > (dist[j] + 1) ? (dist[j] + 1) : d;
        		d = d > (distNew[j - 1] + 1) ? (distNew[j - 1] + 1) : d;
        		distNew[j] = d;
        	}
        	dist = distNew;
        }
        return dist[n];
    }
	
	public static void main(String [] args) {
		String word1 = "a";
		String word2 = "ab";
	}
}
