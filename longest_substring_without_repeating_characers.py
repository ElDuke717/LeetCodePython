def lengthOfLongestSubstring(str):
    charSet = set()
    l = 0
    max_length = 0
    for chars in str:
        while chars in charSet:
            charSet.remove(str[l])
            l += 1
        charSet.add(chars)
        max_length = max(max_length, len(charSet))
    return max_length

print(lengthOfLongestSubstring('abcabcbb'))
