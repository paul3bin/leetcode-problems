""" Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order."""

# Difficulty: Easy


class Solution:
    def isValid(self, s: str) -> bool:
        mapper = {'(': ')', '[': ']', '{': '}'}
        queue = []
        for bracket in s:
            if bracket in mapper.keys():
                queue.append(mapper[bracket])
            elif bracket in mapper.values():
                if not queue or bracket != queue.pop():
                    return False
        if not queue:
            return True
        else:
            return False
