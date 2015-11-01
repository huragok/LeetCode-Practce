class Solution:
    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def fullJustify(self, words, maxWidth):
        len_words = map(len, words)
        n_words = len(words)
        
        start = 0
        end = 0
        width_total = 0
        text = []
        for idx in range(n_words):
            width_total += len_words[idx]
            end += 1
            if width_total + (end - start - 1) > maxWidth: # This new word cannot be added to the current line
                #print((width_total, end, start))
                width_total -= len_words[idx]
                end -= 1
                if end - start == 1: # Corner case, this line contains only 1 word
                    text.append(words[start] + " " * (maxWidth - width_total))
                else:
                    spaces = self.dstrSpace(maxWidth - width_total, end - start - 1)
                    line = ""
                    for i in range(end - start - 1):
                        line += words[start + i] + " " * spaces[i]   
                    line += words[end - 1]
                    text.append(line)
                    
                start = idx
                end = idx + 1
                width_total = len_words[idx]
        
        # Append the last line
        if end - start == 1: # Corner case, this line contains only 1 word
            text.append(words[start] + " " * (maxWidth - width_total))
        else:
            line = ""
            for i in range(end - start - 1):
                line += words[start + i] + " "
            line += words[end - 1] + " " * (maxWidth - (width_total + end - start - 1))
            text.append(line)
                     
        return text

        
    def dstrSpace(self, n_space, n_divide):
    # Function that evenly divide n_space spaces over n_divide segments
    # @return {integer[]} the number of space in each divide
        floor = n_space / n_divide
        res = n_space - floor * n_divide
        spaces = [floor + 1] * res + [floor] * (n_divide - res)
        return spaces
        
if __name__ == "__main__":
    n_space = 3
    n_divide = 2
    print(Solution().dstrSpace(n_space, n_divide))
    
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    L = 16
    words = ["What","must","be","shall","be."]
    L = 12
    print(Solution().fullJustify(words, L))
