package llw;

public class Solution {
	public int lengthOfLastWord(String s) {
		int n = s.length();
		
		if (n == 0) {
			return 0;
		}
		int i = n - 1;
        for (i = n - 1; i >=0; i--) {
        	if (s.charAt(i) != ' ') {
        		break;
        	}
        }
        if (i < 0) {
        	return 0;
        }
        int j;
        for (j = i; j >= 0; j--) {
        	if (s.charAt(j) == ' ') {
        		break;
        	}
        }
        return i - j;
    }
	
	public static void main(String [] args) {
		String s = "Hello World";
		System.out.println(new Solution().lengthOfLastWord(s));
	}
}
