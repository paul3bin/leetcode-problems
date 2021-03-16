"""Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string('')"""

# Difficulty: Easy

def longestCommonPrefix(strs):
    if strs:
        sort_by_length = lambda string: len(string)
        strs.sort(key=sort_by_length)
        substr_list = [strs[0][:i] for i in range(len(strs[0])+1)]
        common_prefix = []
        for substr in substr_list:
            bool_val = []
            for string in strs[1:]:
                bool_val.append(substr in string[:len(substr)])
            if len(strs[1:]) == bool_val.count(True):
                common_prefix.append(substr)
        if common_prefix:
            return common_prefix[::-1][0]
        return ""
    return ""


print(longestCommonPrefix(["reflower","flow","flight"]))
