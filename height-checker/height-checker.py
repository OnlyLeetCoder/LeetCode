class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        nomatch = 0
        
        for h1, h2 in zip(expected, heights):
            nomatch += 1 if h1 != h2 else 0
        
        return nomatch