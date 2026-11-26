class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1
        result = []
        while left < right and numbers[left] + numbers[right] != target:
            sum = numbers[left] + numbers[right]
            if sum < target:
                left += 1
            elif sum > target:
                right -= 1
        return [left + 1, right + 1]
