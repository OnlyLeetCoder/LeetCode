class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        cnt = 0
        
        for st, en in zip(startTime, endTime):
            if st <= queryTime <= en:
                cnt += 1
        
        return cnt