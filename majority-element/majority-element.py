from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        
        for el in nums:
            if cnt[el] > len(nums)//2:
                return el