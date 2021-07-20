class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        cnt = 0
        
        for type, color, name in items:
            if ruleKey == 'color':
                if color == ruleValue:
                    cnt += 1
            elif ruleKey == 'name':
                if name == ruleValue:
                    cnt += 1
            else:
                if type == ruleValue:
                    cnt += 1
        
        return cnt