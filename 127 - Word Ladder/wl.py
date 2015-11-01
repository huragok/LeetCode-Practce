class Solution:
    # @param {string} beginWord
    # @param {string} endWord
    # @param {set<string>} wordDict
    # @return {integer}
    def ladderLength(self, beginWord, endWord, wordDict):
        n = len(beginWord)
        alpha = set('abcdefghijklmnopqrstuvwxyz')
        q_begin = {beginWord}
        q_end = {endWord}
        len_ladder = 2
        
        while q_begin and q_end:
            print(q_begin, q_end)
            if len(q_begin) < len(q_end): # Update the smaller set since the look up in a set takes O(1) and one needs to try all possible next words from the updated set
                q_update = q_begin
                q_stat = q_end
            else:
                q_update = q_end
                q_stat = q_begin
            q_update_new = set()
            for word in q_update:
                for pos in range(n):
                    letter_curr = word[pos]
                    for letter in alpha:
                        if letter != letter_curr:
                            word_new = word[0:pos] + letter + word[pos+1:]
                            if word_new in q_stat:
                                
                                return len_ladder
                            elif word_new in wordDict:
                                q_update_new.add(word_new)
                                wordDict.remove(word_new)
            
            q_update = q_update_new
            if len(q_begin) < len(q_end):
                q_begin = q_update_new
            else:
                q_end = q_update_new
            len_ladder += 1
            
        return 0
                                
        
if __name__ == "__main__":
    beginWord = "hit"
    endWord = "cog"
    wordDict = ["hot","dot","dog","lot","log"]
    print(Solution().ladderLength(beginWord, endWord, wordDict))
