class Solution:
    def intToRoman(self, num: int) -> str:
        count, roman = 0, ''
        symbol = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M' }
        while num:
            digit, multiple = num % 10, 10 ** count
            if digit >= 5:
                if digit == 9:
                    roman = symbol[1 * multiple] + symbol[10 * multiple] + roman
                else:
                    roman = symbol[5 * multiple] + (digit - 5) * symbol[1 * multiple] + roman
            else:
                if digit == 4:
                    roman = symbol[1 * multiple] + symbol[5 * multiple] + roman
                else:
                    roman = digit * symbol[1 * multiple] + roman
            num //= 10
            count += 1
        return roman

    def intToRoman2(self, num: int) -> str:
        length, roman = len(str(num)), ''
        symbol = { 1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 10000: 'None' }
        for count in range(length):
            digit, multiple= num % 10, 10 ** count
            if 4 <= digit <= 8:
                roman = max(0, (5 - digit)) * symbol[1 * multiple] + symbol[5 * multiple] + max(0, (digit - 5)) * symbol[1 * multiple] + roman
            else:
                roman = min(digit, (10 - digit)) * symbol[1 * multiple] + max(0, (digit - 8)) * symbol[10 * multiple] + roman
            num //= 10
        return roman
