class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def sequence(numRows, length):
            p = []
            while len(p) < length:
                for i in range(1, numRows + 1):
                    p.append(i)
                for i in range(numRows - 1, 1, -1):
                    p.append(i)
            return p[:length]
        ss = ''
        for i, j in sorted(zip(sequence(numRows, len(s)), s), key=lambda x:x[0]):
            ss += j
        return ss
