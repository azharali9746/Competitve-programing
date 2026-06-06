"""
Problem: LeetCode 268 — Missing Number
Given an array of n distinct numbers in the range [0, n],
return the one missing number.
Example: [3,0,1] → 2  (n=3, expected sum=6, actual sum=4, missing=2)

Approach:
Mathematical — Sum Formula.
- The sum of integers from 0 to n is: n * (n + 1) / 2  (Gauss formula).
- Subtract the actual sum of the array from the expected sum.
- The difference is the missing number.

Time Complexity: O(n) — one pass to compute actual sum.
Space Complexity: O(1) — only two integer accumulators.
"""

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Compute the actual sum of elements present in the array
        expected = 0
        for i in nums:
            expected = expected + i   # 'expected' here holds the actual array sum

        # Length n — the array should contain numbers from 0 to n
        l = len(nums)

        # Compute what the sum SHOULD be: 0 + 1 + 2 + ... + n
        actual = l * (l + 1) // 2

        # The missing number is the difference between expected total and actual sum
        return actual - expected
