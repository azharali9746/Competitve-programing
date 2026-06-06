"""
Problem:
Given an array of integers, reverse the entire array in-place.
Example: [1, 2, 3, 4, 5] → [5, 4, 3, 2, 1]

Approach:
Two Pointers (In-place Swap).
- Use index i from 0 to mid (l//2).
- Swap element at i with its mirror element at (l-i-1).
- Stop at the midpoint — each swap handles two positions.

Time Complexity: O(n/2) = O(n)
Space Complexity: O(1) — swapped in-place using a temp variable.
"""

# Read the array from user input
a = list(map(int, input().split()))
l = len(a)

# Swap elements from both ends moving toward the center
for i in range(l // 2):
    # Store the element from the right end temporarily
    temp = a[l - i - 1]

    # Place the left element at the mirrored right position
    a[l - i - 1] = a[i]

    # Place the saved right element at the left position
    a[i] = temp

# Print the reversed array
print(a)
