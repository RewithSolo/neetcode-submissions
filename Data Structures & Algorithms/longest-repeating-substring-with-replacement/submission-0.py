class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        res = 0
        hset = {}
        for right in range(len(s)):
            if s[right] in hset:
                hset[s[right]] += 1
            else:
                hset[s[right]] = 1
            max_freq = max(hset.values())

            if (right - left + 1) - max_freq > k:
                hset[s[left]] -= 1
                left += 1
            
            res = max(res, right - left + 1)

        return res