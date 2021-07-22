class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0
        
        for word in words:
            if all(ch in allowed for ch in word):
                cnt += 1
        
        return cnt