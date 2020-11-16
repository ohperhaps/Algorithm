class Solution:
    def threeSumClosest(self, nums, target) -> int:
        nums.sort()
        distance = None
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if distance is None or abs(sum - target) < distance:
                    distance = abs(sum - target)
                    result = sum
                if sum < target:
                    l += 1
                elif sum > target:
                    r -= 1
                else:
                    return target
        return result
