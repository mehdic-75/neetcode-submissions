class Solution:
    def hammingWeight(self, n: int) -> int:
        total = 0
        while n > 0:
            total += n % 2   
            n = n // 2       
        return total
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n+1):
            output.append(self.hammingWeight(i))
        return output