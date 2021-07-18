class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        kidWithMaxCandies = max(candies)
        
        boolArr = [False] * len(candies)
        
        for i, el in enumerate(candies):
            boolArr[i] = (el + extraCandies >= kidWithMaxCandies)
        
        return boolArr