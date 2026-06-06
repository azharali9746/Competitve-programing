"""
Problem: LeetCode 66 — Plus One
Given a non-empty array of digits representing a non-negative integer,
increment the integer by one and return the result as an array of digits.
Example: [1,2,9] → [1,3,0]  |  [9,9,9] → [1,0,0,0]

Approach:
Reverse traversal with carry propagation.
- Start from the last digit (least significant).
- If the digit is 9, set it to 0 and carry over (continue loop).
- If the digit is not 9, simply increment it and return immediately.
- If all digits were 9 (all became 0), prepend 1 to the array.

Time Complexity: O(n) — in the worst case (all 9s), all digits are visited.
Space Complexity: O(1) — modified in-place (O(n) only for the [1]+digits case).
"""

from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Traverse from the last digit to the first
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                # Current digit is 9 → becomes 0 and carry propagates left
                digits[i] = 0
            else:
                # No carry — just increment and we're done
                digits[i] += 1
                return digits

        # If we exit the loop, all digits were 9 (now all 0s)
        # Prepend 1 to handle the overflow (e.g. [9,9] → [1,0,0])
        return [1] + digits
