package ab;

public class Solution {
	public String addBinary(String a, String b) {
        int m = a.length();
        int n = b.length();
        int l = m > n ? m : n;
        int carryOn = 0;
        
        String result = "";
        for (int i = 0; i < l; i++) {
        	int d = carryOn;
        	if (i < m && a.charAt(n - 1 -i) == '1') {
        		d += 1;
        	}
        	if (i < n && b.charAt(m - 1 - i) == '1') {
        		d += 1;
        	}
        	if (d % 2 == 1) {
        		result = "1" + result;
        	} else {
        		result = "0" + result;
        	}
        	carryOn = d / 2;
        }
        if (carryOn > 0) {
        	result = "1" + result;
        }
        return result;
    }
	
	public static void main(String [] args) {
		String a = "1010";
		String b = "1011";
		System.out.println(new Solution().addBinary(a, b));
	}
}
