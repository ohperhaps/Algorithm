class Solution:
    def threeSum(self, nums):
        # O(n^3)
        result = []
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    threenums = (nums[i], nums[j], nums[k])
                    if not sum(threenums) and sorted(list(threenums)) not in result:
                        result.append(sorted(list(threenums)))
        print(len(result))
        return result

    def threeSum2(self, nums):
        # O(NlogN+N^2) ~= O(N^2)
        result = []
        nums.sort()  # sorted: min - max
        for i in range(len(nums) - 2):
            # if nums[i] > 0 then sum  > 0
            if nums[i] > 0:
                break
            # 1. skip num is same to front num
            # 2. Do not skip a series of same nums at the beginning.
            if i > 0 and nums[i] == nums[i-1]:
                continue
            # l(left) is the min num greater than num[i], r(right) is the max num greater than num[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                # sum < 0, left pointer right shift to make sum larger
                if sum < 0:
                    l += 1
                # sum > 0, right pointer left shift to make sum smaller
                elif sum > 0:
                    r -= 1
                else:
                    # sum = 0
                    result.append([nums[i], nums[l], nums[r]])
                    # move l and r to next different numbers.
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1
                    r -= 1
        return result

