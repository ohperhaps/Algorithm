class Solution:
    def longestCommonPrefix(self, strs) -> str:
        longest = len(min(strs, key=len)) if strs else 0
        for i in range(1, len(strs)):
            for j in range(longest):
                if not strs[i - 1][j] == strs[i][j]:
                    longest = j
                    break
            if not longest:
                break
        return strs[0][:longest] if longest else ''

    def longestCommonPrefix2(self, strs) -> str:
        shortest = min(strs, key=len) if strs else ''
        for i, v in enumerate(shortest):
            for str_ in strs:
                if str_[i] != v:
                    return shortest[:i]
        return shortest
