class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        t_contain = {}
        win_contain = {}
        have = 0
        right_min = 0
        left_min = 0
        res_min = float("inf")
        
        for sym in t:
            if sym in t_contain:
                t_contain[sym] += 1
            else:
                t_contain[sym] = 1
                win_contain[sym] = 0
        
        need = len(t_contain)
    
        for right in range(len(s)):
            if s[right] in win_contain:
                win_contain[s[right]] += 1
            else:
                win_contain[s[right]] = 1
            if s[right] in t_contain and win_contain[s[right]] == t_contain[s[right]]:
                have += 1

            while have == need:
                if right - left + 1 < res_min:
                    res_min = right - left + 1
                    right_m = right
                    left_m = left
                
                win_contain[s[left]] -= 1
                if s[left] in t_contain and win_contain[s[left]] < t_contain[s[left]]:
                    have -= 1
                
                left += 1
        
        if res_min == float("inf"):
            return ""
        
        return s[left_m:right_m + 1]




