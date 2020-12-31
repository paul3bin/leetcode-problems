"""Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward."""

# Difficulty: Easy

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x==int(str(abs(x))[::-1])