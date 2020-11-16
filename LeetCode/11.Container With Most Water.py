class Solution:
    def maxArea(self, height) -> int:
        maxarea = 0
        for i in range(len(height) - 1):
            for j in range(i + 1, len(height)):
                    maxarea = max(min(height[i], height[j]) * (j - i), maxarea)
        return maxarea

    def maxArea2(self, height) -> int:
        ls = sorted(enumerate(height), key=lambda x: x[1], reverse=True)
        left, right = min(ls[1][0], ls[0][0]), max(ls[1][0], ls[0][0])
        for tp in ls[2:]:
            if tp[0] < left and (left - tp[0]) * tp[1] > (right - left) * (min(height[right], height[left]) - height[tp[0]]):
                left = tp[0]
            elif tp[0] > right and (tp[0] - right) * tp[1] > (right - left) * (min(height[right], height[left]) - height[tp[0]]):
                right = tp[0]
        maxarea = (right - left) * min(height[right], height[left])
        for i in range(0, left + 1):
            for j in range(right, len(height)):
                maxarea = max((j - i) * min(height[j], height[i]), maxarea)
        return int(maxarea)

    def maxArea3(self, height) -> int:
        left, right, width, maxarea = 0, len(height) - 1, len(height) - 1, 0
        for w in range(width, 0, -1):
            maxarea = max(min(height[left], height[right]) * w, maxarea)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxarea
