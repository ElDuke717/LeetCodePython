class Solution:
    def romanToInt(self, s: str) -> int:
        roman_map = {     
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
        }
        if len(s) == 1: 
            return roman_map[s[0]]
        res = 0
        i = 0
        while i < len(s):
            if i + 1 < len(s) and roman_map[s[i]] < roman_map[s[i + 1]]:
                    res += roman_map[s[i + 1]] - roman_map[s[i]]
                    i += 2  # Skip the next character since we've processed it
            else:
                res += roman_map[s[i]]
                i += 1

        return res

# Create an instance of the class
solution_instance = Solution()

# Call the method on the instance
print(solution_instance.romanToInt('III'))

