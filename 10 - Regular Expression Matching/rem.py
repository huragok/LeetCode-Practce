#!/usr/bin/env python

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        M = len(s) # Length of the string
        N = len(p) # Length of the pattern
            
        # Indicator of whether s[0:m] is matched to p[0:n]
        flag = [[False for n in range(N+1)] for m in range(M+1)]
        
        # Initialization
        flag[0][0] = True
        if N > 0:
            flag[0][1] = False
        for n in range(2, N+1):
            if p[n - 1] == '*' and flag[0][n-2]:
                flag[0][n] = True
                
        # Start the iteration
        for m in range(1, M+1):
            for n in range(1, N+1):
                # The first case: s[m - 1] is matched to p[n - 1] which is a character
                # The second case: s[m - 1] is matched to p[n - 1] which is a '.'
                if (s[m-1] == p[n-1] or p[n-1] == '.'):
                    flag[m][n] = flag[m-1][n-1]  
                elif p[n-1] == '*': # The third case: s[m - 1] is matched to p[n - 1] which is a '*'
                    if p[n-2] != '.': # If the preceding is a normal character, say 'a'
                        if flag[m][n-2]: #'a*' in p is not matched to anything in s
                            flag[m][n] = True
                        elif s[m-1] == p[n-2]: # 'a*' in p is matched to the end of s
                            for i in range(m): # The last few characters in s must all be 'a'
                                 if flag[i][n-2] and all(c == p[n-2] for c in s[i : m]):
                                    flag[m][n] = True
                                    break
                    else: # the preceding character is '.' p[0:n-2] is matched to any s[0:m-k], k>=0
                        for i in range(m + 1):
                            if flag[i][n-2]:
                                flag[m][n] = True
                                break
                                
        #for m in range(M+1):
         #   for n in range(N+1):
          #      print((m,n))
           #     print(flag[m][n])
        return flag[M][N]
        
if __name__ == "__main__":
    sp = [('aa', 'a'), ('aa', 'aa'), ('aaa', 'aa'), ('aa', 'a*'), ('aa', '.*'), ('ab', '.*'), ('aab', 'c*a*b'), ('a', ''), ('abcd', 'd*'), ('aaa', 'ab*ac*a'), ('aaa', 'ab*a*c*a'), ("aaba", "ab*a*c*a"), ("aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"), ("baabbbaccbccacacc", "c*..b*a*a.*a..*c")]
    #sp = [('aaa', 'ab*a*c*a')]
    #sp = [('aa', 'ab*a*')]
    #sp = [("aab", "ab*")]
    #sp = [("aasdf", "aasdf.*")]
    #sp = [("baabbbaccbccacacc", "c*..b*a*a.*a..*c")]
    sol = Solution()
    for s, p in sp:
        print("isMatch({0}, {1}) -> {2}".format(s, p, sol.isMatch(s, p)))
                    
                
               
