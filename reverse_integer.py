"""Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: 
[−231,  231 − 1]. For the purpose of this problem, 
assume that your function returns 0 when the reversed integer overflows.
"""

# Difficulty: Easy

class Solution:
    def reverse(self, x: int) -> int:
        if int(str(abs(x))[::-1])>((2**31)-1) or -int(str(abs(x))[::-1])<(-2**31):
            return 0
        elif x < 0:
            return -int(str(abs(x))[::-1])
        else:
            return int(str(abs(x))[::-1])