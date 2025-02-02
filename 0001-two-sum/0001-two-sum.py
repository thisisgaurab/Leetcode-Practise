class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numSet = {}

        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in numSet:
                return [i, numSet[rem]]
            
            numSet[nums[i]] = i

        return []