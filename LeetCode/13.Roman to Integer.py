class Solution:
    def romanToInt(self, s: str) -> int:
        def calculate(roman):
            num, minus = symbol[roman[-1]], -1 if symbol[roman[-1]] > symbol[roman[0]] else 1
            for j in roman[:-1]:
                num += minus * symbol[j]
            return num

        s, result = '^' + s + '$', 0
        symbol = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M':1000, '^': 0, '$': 0}
        for i in range(1, len(s) - 1):
            if i == len(s) - 2:
                return calculate(s[1:-1])
            elif symbol[s[i - 1]] <= symbol[s[i]] > symbol[s[i + 1]]:
                return calculate(s[1:i + 1]) + self.romanToInt(s[i + 1:-1])

    def romanToInt2(self, s: str) -> int:
        d, res, p= {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}, 0, 'I'
        for c in s[::-1]:
            res, p = res - d[c] if d[c] < d[p] else res + d[c], c
        return res