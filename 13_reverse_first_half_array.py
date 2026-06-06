"""
Problem:
Given an array, reverse only the first half of it (in-place).
Example: [1, 2, 3, 4, 5, 6] → [3, 2, 1, 4, 5, 6]

Approach:
Two Pointers on the first half only.
- Find the midpoint l2 = l // 2.
- Swap elements at i and (l2 - i - 1) for i in range(l2 // 2).
- Only the first l2 elements are affected.

Time Complexity: O(n/4) = O(n)
Space Complexity: O(1)
"""

# Read the array from user input
a = list(map(int, input().split()))
l = len(a)

# Find the midpoint index (length of the first half to reverse)
l2 = l // 2

# Reverse only the first half using two-pointer swaps
for i in range(l2 // 2):
    # Swap element at position i with its mirror in the first half
    temp = a[l2 - i - 1]
    a[l2 - i - 1] = a[i]
    a[i] = temp

# Print the modified array (only the first half is reversed)
print(a)
