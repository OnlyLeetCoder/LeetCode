class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        replies = []
        
        for i in range(1, n+1):
            if i % 3 == 0 and i % 5 == 0:
                replies.append("FizzBuzz")
            elif i % 3 == 0:
                replies.append("Fizz")
            elif i % 5 == 0:
                replies.append("Buzz")
            else:
                replies.append(str(i))
        
        return replies