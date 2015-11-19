package rncgr4;

public class Solution extends Reader4 {
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    public int read(char[] buf, int n) {
        int countRead = 0;
        char [] bufTmp = new char [4];
        while (countRead < n) {
        	int r = read4(bufTmp );
        	for (int i = 0; i < r; i++) {
        		buf[countRead] = bufTmp[i];
        		countRead++;
        		if (countRead >= n) {
        			break;
        		}
    		}
        	if (r < 4) {
        		break;
        	}
        }
        return countRead;
    }
}
