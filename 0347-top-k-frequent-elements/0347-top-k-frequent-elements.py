class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for num in nums:
            if num not in dict1:
                dict1[num] = 1
            else:
                dict1[num] += 1

        sorted_nums = sorted(dict1.keys(), key = lambda x:dict1[x], reverse = True)
                
        return sorted_nums[:k]

        
        

        