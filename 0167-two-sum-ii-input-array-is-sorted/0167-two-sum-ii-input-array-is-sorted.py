class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numSet = {}

        for i in range(len(numbers)):
            rem = target - numbers[i]

            if rem in numSet:
                return [numSet[rem]+1, i+1]

            numSet[numbers[i]] = i
        