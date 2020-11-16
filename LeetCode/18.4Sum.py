class Solution:
    def fourSum(self, nums, target):
        nums.sort()
        length, result = len(nums), []
        for i in range(length - 3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i + 1, length - 2):
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                l = j + 1
                r = length - 1
                while l < r:
                    sum = nums[i] + nums[j] + nums[l] + nums[r]
                    if sum < target:
                        l += 1
                    elif sum > target:
                        r -= 1
                    else:
                        result.append([nums[i], nums[j], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l+1]:
                            l += 1
                        while l < r and nums[r] == nums[r-1]:
                            r -= 1
                        l += 1
                        r -= 1
        return result

a = Solution()
print(a.fourSum([1, 0, -1, 0, -2, 2], 0))