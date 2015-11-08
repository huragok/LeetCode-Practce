package is;

public class Solution {
	public boolean isInterleave(String s1, String s2, String s3) {
		int m = s1.length();
		int n = s2.length();
		
		if (m + n != s3.length()) return false;
		if (m == 0) return s3.equals(s2);
		if (n == 0) return s3.equals(s1);
		
		boolean [] isInterleavePartial = new boolean [n + 1]; // isInterleavePartial[i][j] indicates whether s1[0:i] and s2[0:j] interleaves s3[0:i+j]
		isInterleavePartial[0] = true;
		for (int j = 1; j <= n; j++) {
			isInterleavePartial[j] = isInterleavePartial[j - 1] & (s2.charAt(j - 1) == s3.charAt(j - 1));
		}
		
		for (int i = 1; i <= m; i++) {
			boolean last = isInterleavePartial[0];
			isInterleavePartial[0] &= (s1.charAt(i - 1) == s3.charAt(i - 1));
			for (int j = 1; j <= n; j++) {
				last = isInterleavePartial[j];
				isInterleavePartial[j] = (isInterleavePartial[j - 1] & (s2.charAt(j - 1) == s3.charAt(i + j - 1))) || 
										 (last & (s1.charAt(i - 1) == s3.charAt(i + j - 1)));
			}
		}
		
		return isInterleavePartial[n];
    }
	
	public static void main(String [] args) {
		String s1 = "aabcc";
		String s2 = "dbbca";
		String s3 = "aadbbbaccc";
		System.out.println(new Solution().isInterleave(s1, s2, s3));
	}
}
