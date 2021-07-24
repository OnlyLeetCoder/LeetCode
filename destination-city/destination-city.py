from collections import defaultdict

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        outDeg = defaultdict(lambda: 0)
        cities = set()
        
        for cityA, cityB in paths:
            outDeg[cityA] += 1
            cities.add(cityA)
            cities.add(cityB)
        
        for city in cities:
            if outDeg[city] == 0:
                return city