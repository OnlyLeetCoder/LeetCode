class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        neg = 0
        
        for row in grid:
            col_len = len(row)
            i = 0
            while i < col_len:
                if row[i] < 0:
                    break
                i += 1
            
            neg += col_len - i
        
        return neg