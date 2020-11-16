class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairs2(self, n):
        a = b = 1
        for i in range(n):
            a, b = b, a + b
        return a