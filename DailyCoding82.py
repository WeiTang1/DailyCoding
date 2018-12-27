from Queue import Queue


class Solution(object):
    def __init__(self):
        # self.curTotal = 0
        self.buffer = Queue()
        self.endOfFile = False

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 0:
            return 0

        total = 0
        while self.buffer.qsize() < n and not self.endOfFile:
            temp = [""] * 4
            r = read4(temp)
            if r < 4:
                self.endOfFile = True
            for i in range(r):
                self.buffer.put(temp[i])

        for i in range(min(self.buffer.qsize(), n)):
            buf[i] = self.buffer.get()
            total += 1

        return total