class Solution:
    def trap(self, height: List[int]) -> int:
        left_m = 0
        right_m = 0
        left = 0
        right = len(height) - 1
        res = 0
        while left < right:
            left_m = max(left_m, height[left])
            right_m = max(right_m, height[right])
            if left_m < right_m:
                res += left_m - height[left]
                left += 1
            else:
                res += right_m - height[right]
                right -= 1

        return res