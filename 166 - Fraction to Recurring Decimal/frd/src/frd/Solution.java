package frd;

import java.util.Map;
import java.util.HashMap;
import java.util.List;
import java.util.ArrayList;

public class Solution {
	public String fractionToDecimal(int numerator, int denominator) {
		long num = numerator;
		long den = denominator;
		String sign = (num * den >= 0 ? "" : "-");
		if (num < 0) num = -num;
		if (den < 0) den = -den;
        
		long itg = num / den; // The integer part
        num -= itg * den;
        if (num == 0) return sign + Long.toString(itg);
        
        long residual = num * 10;
        Map<Long, Integer> idx = new HashMap<Long, Integer> (); // Map numerator to idx
        int i = 0;
        List<Long> frac = new ArrayList<Long> ();
        
        while (residual > 0) {
        	if (idx.containsKey(residual)) {
        		break;
        	} else {
        		long d = residual / den;
        		frac.add(d);
        		idx.put(residual, i);
        		residual = 10 * (residual - d * den);
        	}
        	i++;
        }
        String s = Long.toString(itg) + ".";
        if (residual == 0) { // 	
        	for (long digit: frac) {
        		s += Long.toString(digit);
        	}
        } else {
        	for (int j = 0; j < idx.get(residual); j++) {
        		s += Long.toString(frac.get(j));
        	}
        	s += "(";
        	for (int j = idx.get(residual); j < i; j++) {
        		s += Long.toString(frac.get(j));
        	}
        	s += ")";
        }
    	return sign + s;
    }
	
	public static void main(String [] args) {
		int numerator = -1, denominator = -2147483648;
		System.out.println(new Solution().fractionToDecimal(numerator, denominator));
	}
}
