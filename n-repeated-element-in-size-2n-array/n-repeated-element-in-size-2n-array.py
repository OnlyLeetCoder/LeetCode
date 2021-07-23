from collections import Counter

class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        cnt = Counter(nums)
        
        for el in cnt:
            if cnt[el] == len(nums)//2:
                return el