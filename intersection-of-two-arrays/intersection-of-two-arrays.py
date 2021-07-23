class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersec = set()
        
        for el in nums1:
            if el in nums2:
                intersec.add(el)
        
        return list(intersec)