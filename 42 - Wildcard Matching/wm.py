class Solution:
    # @param {string} s
    # @param {string} p
    # @return {boolean}
    def isMatch(self, s, p):
        M = len(s) # length of the string
        N = len(p) # length of the pattern
        
        if N - p.count('*') > M:
            return False
        
        match = [False] * (M + 1) # whether s[0:m] matches p[0:n]
        
        # Initialization
        match[0] = True
                
        # Now let the iteration begin
        for n in range(1, N + 1):
            #print(match)
            a = p[n - 1]
            if a == '?':
                for m in range(M, 0, -1):
                    match[m] = match[m - 1]
            elif a != '*':
                for m in range(M, 0, -1):
                    if s[m - 1] == a:
                        match[m] = match[m - 1]
                    else:
                        match[m] = False
            else:
                for m in range(1, M + 1):
                    match[m] = match[m-1] or match[m]
            
            match[0] = match[0] and a == '*'
            print(match)  
        return match[M]
        
if __name__ == "__main__":
    s = 'aa'
    p = 'aa'
    print(Solution().isMatch(s, p))
