"""Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice."""

# Difficulty: Easy


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for i in range(len(nums)):
            if (target-nums[i]) in nums[i+1:]:
                return [i, nums[i+1:].index(target-nums[i])+i+1]
            elif (target-nums[i]) in nums[:i]:
                return [i, nums[:i].index(target-nums[i])]
