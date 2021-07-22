class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        oddSum = 0
        
        for l in range(1, len(arr)+1, 2):
            for j in range(len(arr)-l+1):
                print(arr[j:j+l])
                oddSum += sum(arr[j:j+l])
        
        return oddSum