class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        arr = defaultdict(list)
        for cur in strs:
            srt = ''.join(sorted(cur))
            arr[srt].append(cur)
        return list(arr.values())