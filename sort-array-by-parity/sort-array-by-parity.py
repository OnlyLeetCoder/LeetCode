class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        ind = 0
        
        for i in range(len(nums)):
            if nums[i] % 2:
                continue
            
            nums[ind], nums[i] = nums[i], nums[ind]
            ind += 1
        
        return nums