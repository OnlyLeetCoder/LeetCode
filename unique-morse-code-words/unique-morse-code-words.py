class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        uniq = set()
        
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        for word in words:
            rep = ''
            for ch in word:
                rep += morse[ord(ch)-ord('a')]
            uniq.add(rep)
        
        return len(uniq)