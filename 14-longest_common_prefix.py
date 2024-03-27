# Define a function to find the longest common prefix among a list of strings
def longestCommonPrefix(strs):
    # If the list is empty, return an empty string as there's no common prefix
    if len(strs) == 0:
        return ''
    # Initialize the prefix to be the first string in the list,
    # as the common prefix cannot be longer than any string in the list.
    prefix = strs[0]
    # Iterate through all the strings in the list starting from the first
    for i in range(len(strs)):
        # If the current string does not start with the current prefix,
        # reduce the prefix by one character at a time until it does.
        # This loop continues as long as the prefix is not found at the start of strs[i].
        while strs[i].find(prefix) != 0:
            prefix = prefix[:-1]  # Remove the last character from the prefix
            # If the prefix becomes an empty string, it means there's no common prefix.
            # Return an empty string in this case.
            if prefix == '':
                return ''
    # After checking all strings, return the longest common prefix found.
    return prefix

# Test the function with two lists of strings
strs1 = ["flower","flow","flight"]
strs2 = ["dog","racecar","car"]
print(longestCommonPrefix(strs1)) # Should print "fl" as the longest common prefix
print(longestCommonPrefix(strs2)) # Should print "" as there is no common prefix


"""
This function works by initially assuming the whole first string is the common prefix, then progressively shortening that prefix until all strings in the list start with it. If the prefix is reduced to an empty string, it indicates there is no common prefix, and the function returns an empty string immediately.

"""