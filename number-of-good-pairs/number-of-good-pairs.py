class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodCnt = 0
        
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    goodCnt += 1
        
        return goodCnt