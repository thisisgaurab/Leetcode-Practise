from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = defaultdict(int)
        for num in nums:
            d[num] += 1     # {1:3, 2:2, 3:1}
        
        # created a bucket
        freq = [[] for i in range(len(nums) +1)] 

        for key, val in d.items():   # {(1, 3), (2, 2), (3, 1)}
            freq[val].append(key)

        res = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
            if len(res) == k:
                return res



        
       

        
        

        