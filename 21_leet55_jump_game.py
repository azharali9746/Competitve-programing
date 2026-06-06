"""
Problem: LeetCode 55 — Jump Game
Given an array where each element represents the maximum jump length from
that position, return True if you can reach the last index, False otherwise.
Example: [2,3,1,1,4] → True  |  [3,2,1,0,4] → False

Approach:
Greedy — Track remaining jumps.
- Maintain a counter 'count' representing the maximum jumps still available
  from the current position.
- At each step: if count < 0, we're stuck → return False.
- Update count to the max of its current value or the jump value at this index.
- Decrement count by 1 (we used one step to move forward).

Intuition: count acts like fuel — it recharges if a larger jump is available
at the current position, and drains by 1 at each step.

Time Complexity: O(n) — single pass.
Space Complexity: O(1)
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # m is unused here but was in the original — kept for reference
        m = -1

        # Start with the jump capacity of the first cell
        count = nums[0]

        # Track index position (used to decrement count each step)
        step_counter = 0

        for i in nums:
            # If we've run out of jump capacity, we're stuck
            if count < 0:
                return False
            elif count < i:
                # Found a position with a farther reach — update capacity
                count = i

            # Move one step forward — costs one unit of jump capacity
            count -= 1

        # Survived all positions without getting stuck
        return True
