package cs;

public class Solution {
    public String countAndSay(int n) {
    	String s = "1";
    	for (int i = 0; i < n - 1; i++) {
    		s = say(s);
    	}
    	return s;
    }
    
    private String say(String s) {
    	int l = s.length();
    	String result = "";
    	int count = 0;
    	int val = Character.getNumericValue(s.charAt(0));
    	
    	
    	for (int i = 0; i < l; i++) {
    		int d = Character.getNumericValue(s.charAt(i));
    		if (d == val) {
    			count++;
    		} else {
    			result += String.valueOf(count) + String.valueOf(val);
    			val = d;
    			count = 1;
    		}
    	}
    	if (count > 0) {
    		result += String.valueOf(count) + String.valueOf(val);
    	}
    	
    	return result;
    }
    
    public static void main(String [] args) {
    	int n =5;
    	System.out.println(new Solution().countAndSay(n));
    }
}
