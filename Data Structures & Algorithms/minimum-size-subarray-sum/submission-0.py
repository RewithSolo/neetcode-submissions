class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        res_min = float("inf")
        l_min = 0
        r_min = 0
        cur = 0
        for right in range(len(nums)):
            cur += nums[right]
            while cur >= target:
                if right - left + 1 < res_min:
                    res_min = right - left + 1
                    r_min = right
                    l_min = left
                
                cur -= nums[left]
                left += 1
        
        if res_min == float("inf"):
            return 0
        
        return res_min
          