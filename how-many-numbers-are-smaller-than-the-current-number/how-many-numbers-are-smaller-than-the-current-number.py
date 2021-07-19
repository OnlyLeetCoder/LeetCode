class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        
        for i in range(n):
            now = nums[i]
            cnt = 0
            for el in nums:
                if el < now:
                    cnt += 1
            
            ans[i] = cnt
        
        return ans