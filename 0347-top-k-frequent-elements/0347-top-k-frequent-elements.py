from collections import defaultdict
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        d = defaultdict(int)
        for num in nums:
            d[num] += 1

        # Step 2: Create frequency buckets
        freq = [[] for _ in range(len(nums) + 1)]
        for key, val in d.items():
            freq[val].append(key)

        # Step 3: Collect top k frequent elements
        res = []
        for i in range(len(freq) - 1, 0, -1):  # Start from highest frequency
            for n in sorted(freq[i]):  # Sort elements within the same frequency
                res.append(n)
                if len(res) == k:
                    return res
