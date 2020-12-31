"""Given a string s, find the length of the longest substring without repeating characters. """

# Difficulty: Medium

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique_characters = []
        longest = []
        for character in s:
            if character not in unique_characters:
                unique_characters.append(character)
            else:
                longest.append(len(unique_characters))
                unique_characters = unique_characters[unique_characters.index(character)+1:]
                unique_characters.append(character)
                
        longest.append(len(unique_characters))
        return max(longest)