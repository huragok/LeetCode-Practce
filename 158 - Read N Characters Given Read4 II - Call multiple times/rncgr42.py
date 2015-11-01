# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    def __init__(self):
        self.buf_from_last = []
        
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    def read(self, buf, n):
        len_from_last = len(self.buf_from_last)
        
        if len_from_last >= n: # No need to read from the buf, one can just use the part from the last read
            for idx in xrange(len_from_last):
                buf[idx] = self.buf_from_last[idx]
                
            self.buf_from_last = self.buf_from_last[n : ]
            return n
        else: # Read the part from the last time first, then read from buf
            for idx in xrange(len_from_last):
                buf[idx] = self.buf_from_last[idx]
            count = len_from_last
            buf4 = [""] * 4
            while count < n:
                c = read4(buf4)
                for idx in xrange(min([c, n - count])):
                    buf[count + idx] = buf4[idx]
                count += c
                if c < 4:
                    break
            self.buf_from_last = buf4[n - (count - c): c]
            return min([count, n])
