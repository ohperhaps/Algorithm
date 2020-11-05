import math
class Solution:
    def judgeSquareSum(self, c):
        m, n = 0, int(c**0.5)
        while m <= n:
            sum = m*m + n*n
            if sum < c:
                m+=1
            elif sum > c:
                n-=1
            else:
                return True
        return False

