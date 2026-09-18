class Solution(object):
    def isPalindrome(self, s):
        new_s = ''.join([x.lower() for x in s if x.isalnum()])
        left = 0
        right = len(new_s) - 1

        while left <= right:
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1
        
        return True
         