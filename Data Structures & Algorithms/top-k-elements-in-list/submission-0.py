class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequence = {}
        
        for elem in set(nums):
            frequence.update({elem : nums.count(elem)})
        sorted_freq = dict(sorted(frequence.items(),key=lambda item: item[1], reverse=True))
        elements = list(sorted_freq.keys())[:k]
        return elements