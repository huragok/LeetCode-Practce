package tj;

import java.util.List;
import java.util.ArrayList;

public class Solution {
	public List<String> fullJustify(String[] words, int maxWidth) {
		int n = words.length;
		List<String> result = new ArrayList<String> ();
        int iNextWord = 0;
        while (iNextWord < n) {
        	
        	int wordWidth = 0;
        	int wordCount = 0;
        	for (int i = iNextWord; i < n; i++) {
        		if (wordWidth + words[i].length() + wordCount > maxWidth) break;
        		wordWidth += words[i].length();
        		wordCount++;
        	}
        	
        	if (iNextWord + wordCount == n) { // last line
        		String line = "";
        		for (int i = 0; i < wordCount; i++) {
        			line += words[iNextWord + i];
        			line += " ";
        		}
        		if (line.length() > maxWidth) { // An extra space in the end
        			line = line.substring(0, maxWidth); 
        		} else { // Pad space to the end
        		    int spacePad = maxWidth - line.length();
        			for (int i = 0; i < spacePad; i++) {
        				line += " ";
        			}
        		}
        		result.add(line);
        	} else { // not the last line
        		if (wordCount == 1) { // Only 1 word in the line
        			if (wordWidth == maxWidth) { // This word fills the line, no padding spaces
        				String line = words[iNextWord];
        				result.add(line);
        			} else { // Left align, pad zero to the right
        				String line = words[iNextWord];
        				for (int i = 0; i < maxWidth - words[iNextWord].length(); i++) {
            				line += " ";
            			}
        				result.add(line);
        			}
        		} else { // more than 1 word in the line
        			int spaceCount = wordCount - 1;
        			int spaceWidth = maxWidth - wordWidth;
        			int lenSpaceShort = spaceWidth / spaceCount; // the length of the shorter spaces in this line
        			int nSpaceLong = spaceWidth - lenSpaceShort * spaceCount; // Number of longer spaces in this line
        			String line = words[iNextWord];
        			for (int i = 0; i < nSpaceLong; i++) {
        				for (int j = 0; j < lenSpaceShort + 1; j++) {
        					line += " ";
        				}
        				line += words[iNextWord + i + 1];
        			}
        			for (int i = nSpaceLong; i < spaceCount; i++) {
        				for (int j = 0; j < lenSpaceShort; j++) {
        					line += " ";
        				}
        				line += words[iNextWord + i + 1];
        			}
        			result.add(line);
        		}
        	}
        	iNextWord += wordCount;
        }
        
        return result;
    }
	
	public static void main(String [] args) {
		String [] words = {"Listen","to","many,","speak","to","a","few."};
		int maxWidth = 6;
		System.out.println(new Solution().fullJustify(words, maxWidth));
	}
}
