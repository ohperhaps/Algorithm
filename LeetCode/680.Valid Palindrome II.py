class Solution:
    def validPalindrome(self, s):
        def isPalindrome(ss):
            pointer1, pointer2 = 0, len(ss) - 1
            while pointer1 <= pointer2:
                if ss[pointer1] == ss[pointer2]:
                    pointer1 += 1
                    pointer2 -= 1
                else:
                    return pointer1, pointer2
            return True

        result = isPalindrome(s)
        if result is not True:
            if isPalindrome(s[result[0]+1:result[1]+1]) is not True and isPalindrome(s[result[0]:result[1]]) is not True:
                return False
        return True

