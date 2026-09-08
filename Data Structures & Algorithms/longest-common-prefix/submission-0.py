class Solution(object):
    def longestCommonPrefix(self, strs):
        res = ""
        for i, q in enumerate(zip(*strs)):
            if len(set(q)) == 1:
                res += q[0]
            else:
                break
        return res