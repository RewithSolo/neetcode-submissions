class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        res = 0
        hset = set()
        for right in range(len(s)):
            while s[right] in hset:
                hset.remove(s[left])
                left += 1
            
            res = max(res, right - left + 1)
            hset.add(s[right])
        
        return res
