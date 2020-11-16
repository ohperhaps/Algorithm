class Solution:
    def twoSum(self, numbers, target):
        pointer1, pointer2 = 0, len(numbers) - 1
        while True:
            sum = numbers[pointer1] + numbers[pointer2]
            if sum > target:
                pointer2-=1
            elif sum < target:
                pointer1+=1
            else:
                if pointer1 != pointer2:
                    return pointer1 + 1, pointer2 + 1
                else:
                    return
