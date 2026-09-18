class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
        return sorted(cnt.keys(), key=cnt.get, reverse=True)[:k]
