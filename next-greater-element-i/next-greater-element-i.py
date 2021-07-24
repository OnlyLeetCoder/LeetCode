class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        results = []
        
        for el in nums1:
            ind = nums2.index(el)
            res = -1
            
            for i in range(ind, len(nums2)):
                if nums2[i] > el:
                    res = nums2[i]
                    break
            
            results.append(res)
        
        
        return results