"""
Problem:
Given an array, right-rotate it by 1 position.
Example: [1, 2, 3, 4, 5] → [5, 1, 2, 3, 4]

Approach:
Single-step right rotation using a temp variable.
- Save the last element.
- Shift all elements one position to the right (iterate right to left).
- Place the saved last element at index 0.

Note: The original code had a typo — 'spilt()' instead of 'split()'.
      That has been corrected here. Logic is preserved.

Time Complexity: O(n)
Space Complexity: O(1)
"""

# Read the array from user input (original had typo: .spilt() → .split())
l = list(map(int, input().split()))

# Save the last element — it will wrap around to the front
temp = l[len(l) - 1]

# Shift all elements one step to the right (iterate from end to start)
for i in range(len(l) - 1, -1, -1):
    l[i] = l[i - 1]   # Each element takes the value of its left neighbour

# Place the saved last element at the beginning
l[0] = temp

# Print the right-rotated array
print(l)
