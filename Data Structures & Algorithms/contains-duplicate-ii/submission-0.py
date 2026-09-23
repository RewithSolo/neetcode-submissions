class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hset = set()
        for right in range(len(nums)):
            if nums[right] in hset:
                return True
            else:
                hset.add(nums[right])
            
            if len(hset) > k:
                hset.remove(nums[right - k])
        
        return False
        