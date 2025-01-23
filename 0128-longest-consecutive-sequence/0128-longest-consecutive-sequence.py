class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Sort the array
        nums.sort()
        
        max_length = 1
        current_length = 1
        
        # Iterate through the sorted array
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:  # If the current number is consecutive
                current_length += 1
            elif nums[i] != nums[i - 1]:  # If the number is not a duplicate
                max_length = max(max_length, current_length)
                current_length = 1  # Start a new sequence
        
        # Check the last sequence
        max_length = max(max_length, current_length)
        
        return max_length
