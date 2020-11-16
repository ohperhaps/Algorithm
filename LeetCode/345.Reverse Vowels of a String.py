class Solution:
    def reverseVowels(self, s):
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        m, n, ls = 0, len(s) - 1, list(s)
        while m < n:
            if ls[m] in vowels and ls[n] in vowels:
                ls[m], ls[n] = ls[n], ls[m]
                m+=1
                n-=1
            if ls[m] not in vowels:
                m+=1
            if ls[n] not in vowels:
                n-=1
        return ''.join(ls)

