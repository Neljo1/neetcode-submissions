class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # maps value -> index
        
        for i, num in enumerate(nums):
            diff = target - num
            if diff in seen:
                return [seen[diff], i]
            seen[num] = i