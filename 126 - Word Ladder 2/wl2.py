class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, wordStart, wordEnd, wordDict):
        n = len(wordStart)
        alpha = set('abcdefghijklmnopqrstuvwxyz')
        q_start = {wordStart}
        q_end = {wordEnd}
        partial_start = [[wordStart, ]]
        partial_end = [[wordEnd, ]]
        path = []
        
        flag_found = False
        while q_start and q_end:
            q_update = set()
            word_to_remove = set()
            partial_new = []
            #print(q_start, q_end)
            #print(partial_start, partial_end)
            if len(q_start) < len(q_end): # Update the smaller set
                for word in q_start:
                    for pos in range(n):
                        letter_curr = word[pos]
                        for letter in alpha:
                            if letter != letter_curr:
                                word_new = word[0:pos] + letter + word[pos+1:]
                                if word_new in q_end:
                                    flag_found = True
                                    # Concatenate all paths whose two ends match word, word_new
                                    for path_start in partial_start:
                                        if path_start[-1] == word:
                                            for path_end in partial_end:
                                                if path_end[0] == word_new:
                                                    path.append(path_start + path_end)
                                elif word_new in wordDict:
                                    q_update.add(word_new)
                                    for path_start in partial_start: 
                                        if path_start[-1] == word:
                                            partial_new.append(path_start + [word_new])
                                    word_to_remove.add(word_new)
                q_start = q_update
                partial_start = partial_new
                for word in word_to_remove:
                    wordDict.remove(word)
            else:
                for word in q_end:
                    for pos in range(n):
                        letter_curr = word[pos]
                        for letter in alpha:
                            if letter != letter_curr:
                                word_new = word[0:pos] + letter + word[pos+1:]
                                if word_new in q_start:
                                    flag_found = True
                                    # Concatenate all paths whose two ends match word, word_new
                                    for path_end in partial_end:
                                        if path_end[0] == word:
                                            for path_start in partial_start:
                                                if path_start[-1] == word_new:
                                                    path.append(path_start + path_end)
                                elif word_new in wordDict:
                                    q_update.add(word_new)
                                    for path_end in partial_end: 
                                        if path_end[0] == word:
                                            partial_new.append([word_new] + path_end)
                                    word_to_remove.add(word_new)
                q_end = q_update
                partial_end = partial_new
                for word in word_to_remove:
                    wordDict.remove(word)
            
            if flag_found:
                return path
        
        return []        
        
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordDict = ["hot","dot","dog","lot","log"]
    print(Solution().findLadders(beginWord, endWord, wordDict)) 
