class Codec:

    def encode(self, strs):
        """Encodes a list of strings to a single string.
        
        :type strs: List[str]
        :rtype: str
        """
        return '_'.join([str(len(strs))] + [str(len(s)) for s in strs]) + '_' + ''.join(strs)
        

    def decode(self, s):
        """Decodes a single string to a list of strings.
        
        :type s: str
        :rtype: List[str]
        """
        tokens = s.split('_')
        n_strings = int(tokens[0])        
        n_each = list(map(int, tokens[1 : n_strings + 1]))
        l_header = len('_'.join([str(n_strings)] + [str(n) for n in n_each]) + '_')
        string_cat = s[l_header :]
        
        strs = []
        idx = 0
        for n in n_each:
            strs.append(string_cat[idx : idx + n])
            idx += n
        return strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

if __name__ == "__main__":
    strs = ["C#","&","~Xp|F","R4QBf9g=_"]
    inst = Codec()
    s = inst.encode(strs)
    print(inst.decode(s))
