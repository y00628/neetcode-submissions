from collections import Counter, defaultdict

# Revisit

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        return [item[0] for item in counts.most_common(k)]