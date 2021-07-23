class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        maxSq = cnt = 0
        
        for l, w in rectangles:
            maxSq = max(maxSq, min(l, w))
        
        for l, w in rectangles:
            if min(l, w) == maxSq:
                cnt += 1
        
        return cnt