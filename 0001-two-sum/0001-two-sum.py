class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        num_set = {}

        for i, num in enumerate(nums):

            rem = target-num

            if rem in num_set:
                return[num_set[rem], i]

            num_set[num] = i

        return []
        