class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        decompList = []
        
        for i in range(0, len(nums), 2):
            decompList += [nums[i+1]] * nums[i]
        
        return decompList