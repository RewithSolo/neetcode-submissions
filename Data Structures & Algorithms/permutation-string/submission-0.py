class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        left = 0
        k = len(s1)

        s1_contain = [0] * 26
        s2_contain = [0] * 26
        
        for i in range(k):
            s1_contain[ord(s1[i]) - ord('a')] += 1
            s2_contain[ord(s2[i]) - ord('a')] += 1
        
        matches = 0
        for i in range(26):
            if s1_contain[i] == s2_contain[i]:
                matches += 1
            
        for right in range(k, len(s2)):
            if matches == 26:
                return True

            r_ind = ord(s2[right]) - ord('a')
            if s1_contain[r_ind] == s2_contain[r_ind]:
                matches -= 1
            s2_contain[r_ind] += 1
            if s1_contain[r_ind] == s2_contain[r_ind]:
                matches += 1
            
            l_ind = ord(s2[left]) - ord('a')
            if s1_contain[l_ind] == s2_contain[l_ind]:
                matches -= 1
            s2_contain[l_ind] -= 1
            if s1_contain[l_ind] == s2_contain[l_ind]:
                matches += 1
            
            left += 1

        if matches == 26:
            return True
        
        return False
            