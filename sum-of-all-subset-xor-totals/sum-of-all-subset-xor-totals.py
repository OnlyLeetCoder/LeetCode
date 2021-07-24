class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        subsetXor = 0
        
        for i in range(1 << len(nums)):
            currXor = 0
            for j in range(len(nums)):
                if i & (1 << j):
                    currXor ^= nums[j]
            subsetXor += currXor
        
        return subsetXor