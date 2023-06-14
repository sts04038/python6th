from typing import List

class Solution:
    def reverseString(self, s: List[str]) -> None:
        # solution 1 (by me)
        strs = []
        for char in s:
            strs.insert(0, char)
        s[:] = strs

# Create an instance of the Solution class
solution = Solution()

# Call the reverseString method on the instance
s = ['a', 'b', 'c', 'd']
solution.reverseString(s)

# Print the modified list
print(s)
