class Solution:
    def findLongestWord(self, s, d):
        for ss in sorted(d, key=lambda x: (-len(x), x)):
            m, n = 0, 0
            while n < len(ss) and m < len(s):
                if ss[n] == s[m]:
                    m += 1
                    n += 1
                else:
                    m += 1
            if n == len(ss):
                return ss
        return ''
