class Solution:
    def reverse(self, x: int) -> int:
        def boundary_check(num):
            if  -2147483648 < num < 2147483647:
                return True
            return False

        if not boundary_check(x) or x == 0:
            return 0
        minus = True if x < 0 else False
        positive_x = abs(x)
        while not positive_x % 10:
            positive_x //= 10
        reverse_x = ''.join(reversed(str(positive_x)))
        result = int('-' + reverse_x) if minus else int(reverse_x)
        return result if boundary_check(result) else 0
