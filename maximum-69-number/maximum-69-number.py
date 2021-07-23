class Solution:
    def maximum69Number (self, num: int) -> int:
        max69 = num
        num = list(str(num))
        
        for i in range(len(num)):
            if num[i] == '6':
                num[i] = '9'
                max69 = max(max69, int(''.join(num)))
                num[i] = '6'
                
        return max69