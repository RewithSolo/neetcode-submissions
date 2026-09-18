class Solution(object):
    def maxArea(self, height):
        maxvalue = 0
        n = len(height)
        left = 0
        right = n - 1
        while left < right:
            cur = min(height[right], height[left]) * (right - left)
            maxvalue = max(maxvalue, cur)
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return maxvalue 