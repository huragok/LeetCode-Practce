package lsamtdc;

public class Solution {
	public int lengthOfLongestSubstringTwoDistinct(String s) {
        int n = s.length();
        if (n < 3) return n;
        
        char [] values = new char [2];
        int [] idxLast = new int [2];
        int start;
        
        int i = 0;
        while (i < n && s.charAt(i) == s.charAt(0))  i++;
        if (i == n) return n;
        
        values[0] = s.charAt(0); values[1] = s.charAt(i);
        idxLast[0] = i - 1; idxLast[1] = i;
        start = 0;
        
        int lenMax = i + 1;

        for (; i < n; i++) {
        	char c = s.charAt(i);
        	if (c == values[0]) {
        		idxLast[0] = i;
        	} else if (c == values[1]) {
        		idxLast[1] = i;
        	} else {
        		if (i - start > lenMax) lenMax = i - start;
        		if (idxLast[0] > idxLast[1]) { //replace 1
        			start = idxLast[1] + 1;
        			idxLast[1] = i;
        			values[1] = c;
        		} else { // replace 0
        			start = idxLast[0] + 1;
        			idxLast[0] = i;
        			values[0] = c;
        		}
        	}
        }
        if (n - start > lenMax) lenMax = n - start;
        return lenMax;
    }
	
	public static void main(String [] args) {
		String s = "eceba";
		System.out.println(new Solution().lengthOfLongestSubstringTwoDistinct(s));
	}
}
