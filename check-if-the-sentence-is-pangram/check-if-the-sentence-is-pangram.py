import string

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        return all(ch in sentence for ch in string.ascii_lowercase)