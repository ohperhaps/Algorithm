class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        list, num, origin = [], 0, x
        while x:
            list.append(x % 10)
            x //= 10
        for i, v in enumerate(list[::-1]):
            num += v * pow(10, i)
        return True if origin == num else False
