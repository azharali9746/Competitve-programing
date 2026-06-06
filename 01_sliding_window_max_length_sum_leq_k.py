"""
Problem:
Given a list of integers and a value k, find the maximum length of a
contiguous subarray whose sum is less than or equal to k.

Approach:
Sliding Window with Two Pointers.
- Maintain a window [l, r] and expand it by moving r to the right.
- If the window sum exceeds k, shrink it from the left by moving l forward.
- Track the maximum valid window length throughout.

Time Complexity: O(n) — each element is added and removed at most once.
Space Complexity: O(1) — only a few integer variables are used.
"""

# Read the list of integers from user input
lst = list(map(int, input().split()))

# Read the target maximum sum k
k = int(input())

# Initialize the right pointer, left pointer, current sum, and max length
r, l = 0, 0
s = 0   # Current window sum
m = 0   # Maximum valid window length found so far

# Expand the window by moving the right pointer
while r < len(lst):
    # Add the rightmost element to the current window sum
    s += lst[r]

    # Shrink the window from the left if sum exceeds k
    while s > k:
        s -= lst[l]   # Remove leftmost element from window
        l += 1        # Move left pointer forward

    # Calculate current window length and update maximum
    length = r - l + 1
    m = max(m, length)

    # Move right pointer forward to expand the window
    r += 1

# Print the maximum length of a valid subarray
print(m)
