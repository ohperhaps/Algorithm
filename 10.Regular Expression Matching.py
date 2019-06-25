class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memory = {}
        def dp(i, j):
            if (i, j) not in memory:
                if j == len(p):
                    memory[i, j] = i == len(s)
                else:
                    first_match = i < len(s) and p[j] in {s[i], '.'}
                    if j + 1 < len(p) and p[j + 1] == '*':
                        memory[i, j] = dp(i, j + 2) or first_match and dp(i + 1, j)
                    else:
                        memory[i, j] = first_match and dp(i + 1, j + 1)
            return memory[i, j]
        return dp(0, 0)

    def isMatch2(self, s: str, p: str) -> bool:
        """
        :type s: str
        :type p: str
        :rtype: bool

        DP solution:
        M[i][j] denotes if s[0,..,i-1] matches p[0,..,j-1]
        Then the recurisve function of M[i][j] is:
        1. If p[j-1] is a character other than "*" and ".":
            M[i][j] = M[i-1][j-1] && s[i-1] == p[j-1]
        2. If p[j-1] is ".":
            M[i][j] = M[i-1][j-1]
        3. If p[j-1] is "*":
            1) If "*" matches 0 p[j-2]:
                M[i][j] = M[i][j-2]
            2) If "*" matches 1 p[j-2]:
                M[i][j] = M[i][j-1]
            3) If "*" matches multiple p[j-2], M[i][j] is true iff:
                a. s[i-1] == p[j-2] or p[j-2] is ".", and
                b. M[i-1][j] is true
        """
        M = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        M[0][0] = True
        for j in range(2, len(p) + 1):
            if p[j - 1] == '*':
                M[0][j] = M[0][j - 2]

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.':
                    M[i][j] = M[i - 1][j - 1]
                elif p[j - 1] == '*':
                    if M[i][j - 2] or M[i][j - 1] or ((s[i - 1] == p[j - 2] or p[j - 2] == '.') and M[i - 1][j]):
                        M[i][j] = True
                else:
                    M[i][j] = M[i - 1][j - 1] and s[i - 1] == p[j - 1]
        return M[-1][-1]

