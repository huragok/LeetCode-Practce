package rncgr42;

public class Solution extends Reader4{
	/**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
	
	private char [] bufRes = new char [0];
    public int read(char[] buf, int n) {
        if (n <= bufRes.length) {
        	char [] bufResNew = new char [bufRes.length - n];
        	for (int i = 0; i < n; i++) {
        		buf[i] = bufRes[i];
        	}
        	for (int i = n; i < bufRes.length; i++) {
        		bufResNew[i - n] = bufRes[i];
        	}
        	bufRes = bufResNew;
        	return n;
        } else {
        	int count = 0;
        	char [] bufTmp = new char [4];
        	
        	for (int i = 0; i < bufRes.length; i++){
        		buf[i] = bufRes[i];
        		count++;
        	}
        	while (count < n) {
        		int r = read4(bufTmp);
        		int i;
        	
        		for (i = 0; i < r && count < n; i++) {
        			buf[count] = bufTmp[i];
        			count++;
        		}
        		
        		if (count == n) {
        			char [] bufResNew = new char [r - i];
        			for (int j = i; j < r; j++) {
        				bufResNew[j - i] = bufTmp[j];
        			}
        			bufRes = bufResNew;
        			return n;
        		}
        		
        		if (r < 4) {
        			bufRes = new char [0];
        			return count;
        		}
        	}
        	
        	return count;
        }
    }
}
