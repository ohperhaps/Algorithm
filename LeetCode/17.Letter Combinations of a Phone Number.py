class Solution:
    def letterCombinations(self, digits):
        letterbox = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if len(digits) == 0:
            return []
        elif len(digits) == 1:
            return letterbox[digits]
        else:
            result = []
            for letter in letterbox[digits[0]]:
                suffix = self.letterCombinations(digits[1:])
                result += [letter + i for i in suffix]
            return result
