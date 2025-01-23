class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if not nums:
            return 0

        nums = sorted(nums)
        max_length=1
        curr_length = 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]+1:
                curr_length+=1
            elif nums[i] != nums[i-1]:
                max_length = max(max_length, curr_length)
                curr_length = 1

        max_length = max(max_length, curr_length)

        return max_length



            