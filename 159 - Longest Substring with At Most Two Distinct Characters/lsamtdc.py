import collections

class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstringTwoDistinct(self, s):
        n = len(s)
        if n in {0, 1, 2}:
            return n
        freq = collections.defaultdict(int)
        
        ptr_start = 0
        freq[s[ptr_start]] += 1
        count_distinct = 1
        len_max_distinct = 1
        
        for ptr_end in range(1, n):
            freq[s[ptr_end]] += 1
            if freq[s[ptr_end]] == 1:
                count_distinct += 1
            if count_distinct > 2: 
                if ptr_end - ptr_start > len_max_distinct:
                    len_max_distinct = ptr_end - ptr_start
                while count_distinct > 2:
                    freq[s[ptr_start]] -= 1
                    if freq[s[ptr_start]] == 0:
                        count_distinct -= 1
                    ptr_start += 1
        if n - ptr_start > len_max_distinct:
            len_max_distinct = n - ptr_start
                
        return len_max_distinct
        
if __name__=="__main__":
    s = "aac"
    print(Solution().lengthOfLongestSubstringTwoDistinct(s))
        
            
        
