"""
Problem: LeetCode 136 — Single Number
Given a non-empty array where every element appears twice except for one,
find and return that single unique element.

Approach:
Bit Manipulation — XOR.
Key XOR properties exploited:
  - a ^ a = 0       (same numbers cancel each other out)
  - a ^ 0 = a       (XOR with 0 gives the number itself)
  - XOR is commutative and associative

So XOR-ing all elements leaves only the unpaired one.
Example: [4,1,2,1,2] → 4^1^2^1^2 = 4^(1^1)^(2^2) = 4^0^0 = 4

Constraint met: linear runtime O(n), constant space O(1).

Time Complexity: O(n)
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Initialize XOR accumulator to 0 (neutral element for XOR)
        sum = 0

        # XOR every element — duplicate pairs cancel to 0
        for i in nums:
            sum = sum ^ i

        # Only the unique (unpaired) element remains
        return sum
