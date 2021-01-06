"""Given an array of integers nums.

A pair (i,j) is called good if nums[i] == nums[j] and i < j.

Return the number of good pairs."""


# Difficulty: Easy


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        counter=0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]==nums[j] and i<j:
                    counter+=1
        return counter