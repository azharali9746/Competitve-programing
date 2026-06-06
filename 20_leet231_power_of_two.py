"""
Problem: LeetCode 231 — Power of Two
Given an integer n, return True if it is a power of two, False otherwise.
Examples: n=1 → True (2^0), n=16 → True (2^4), n=3 → False

============================================================
APPROACH 1: Loop-based Division
- If n <= 0, immediately return False.
- Keep dividing n by 2 while it is divisible.
- If n reduces to 1, it was a power of two.

Time Complexity: O(log n) — divides by 2 each iteration.
Space Complexity: O(1)

APPROACH 2: Bit Manipulation (Optimal)
- Powers of two in binary have exactly one bit set: 1, 10, 100, 1000, ...
- n - 1 flips all the bits after the set bit: e.g., 8=1000, 7=0111
- n & (n-1) == 0 only when n has exactly one bit set → power of two.

Time Complexity: O(1) — single bitwise operation.
Space Complexity: O(1)
============================================================
"""

# ─── APPROACH 1: Loop-based Division ─────────────────────────────────────────

class SolutionLoop:
    def isPowerOfTwo(self, n: int) -> bool:
        # A power of two must be positive
        if n <= 0:
            return False

        # Keep dividing by 2 as long as n is even
        while n % 2 == 0:
            n = n // 2

        # If what remains is 1, n was originally a power of two
        if n == 1:
            return True
        else:
            return False


# ─── APPROACH 2: Bit Manipulation (Optimal, O(1)) ─────────────────────────────

class SolutionBitwise:
    def isPowerOfTwo(self, n: int) -> bool:
        # n must be positive AND have exactly one bit set in binary
        # n & (n-1) clears the lowest set bit — result is 0 for powers of two
        return n > 0 and (n & (n - 1)) == 0
