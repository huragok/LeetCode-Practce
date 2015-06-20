class Solution:
    # @param {string} s
    # @param {string[]} words
    # @return {integer[]}
    def findSubstring(self, s, words):
        
        l = len(words) # Number of words
        if l == 0:
            return []
            
        k = len(words[0]) # length of each word
        n = len(s) # length of the string
        
        words_set = list(set(words));
        words_count = [words.count(word) for word in words_set]
        l_unique = len(words_set)
        print(words_count)
        print(words_set)
        idx_words = [-1] * (n - k + 1) # An indicator list. idx_words[i] == idx if s[i : i + k - 1] == words[idx], else idx_words[i] == -1
        for i in range(n - k + 1):
            try:
                idx_words[i] = words_set.index(s[i : i + k])
            except ValueError:
                idx_words[i] = -1
        
        #print(idx_words)
        output = []
        print(n - k * (l - 1))
        for i in range(n + 1 - k * l):
            flag_found = True
            count = [0] * l_unique
            for j in range(l):
                if idx_words[i + k * j] < 0:
                    flag_found = False
                    break
                else:
                    count[idx_words[i + k * j]] += 1
            #print(count)
            if flag_found and words_count == count:
                output.append(i)
                
        return output
                
        
                
if __name__ == "__main__":
    s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
    words = ["fooo","barr","wing","ding","wing"]
    s = "a"
    words = ["a"]
    out = Solution().findSubstring(s, words)
        
        
