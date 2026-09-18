class Solution(object):
    def longestConsecutive(self, nums):
        numset = set(nums)
        res = 0
        for num in numset:
            cur = num
            if (cur - 1) in numset:
                continue
            local = 0
            while cur in numset:
                cur += 1
                local += 1

            res = max(local, res)

        return res
        