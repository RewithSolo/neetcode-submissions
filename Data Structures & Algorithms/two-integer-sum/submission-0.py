class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}
        for i, num in enumerate(nums):
            ds = target - num
            if ds in num_map:
                return [num_map[ds], i]
            num_map[num] = i