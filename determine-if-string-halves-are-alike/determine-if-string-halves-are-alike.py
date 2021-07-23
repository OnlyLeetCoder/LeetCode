class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = 'aeiouAEIOU'
        n = len(s)
    
        lcnt = sum(s[:n//2].count(vowel) for vowel in vowels)
        rcnt = sum(s[n//2:].count(vowel) for vowel in vowels)
        
        return lcnt == rcnt
        
            