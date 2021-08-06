class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        ans = []
        
        for word in words:
            for row in rows:
                if all(ch in row for ch in word.lower()):
                    ans.append(word)
        
        return ans
                