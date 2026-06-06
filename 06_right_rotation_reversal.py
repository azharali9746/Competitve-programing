"""
Problem:
Given an array and a value k, rotate the array to the RIGHT by k positions.
Example: [1,2,3,4,5], k=2  →  [4,5,1,2,3]

Approach:
Reversal Algorithm with modular arithmetic.
- First take k % l to handle cases where k >= array length.
- Split the array at index (l - k): left part and right part.
- Reverse each part separately, join them, then reverse the whole.

Key insight: Right rotation by k = Left rotation by (l - k).
The modulo ensures we handle over-rotation gracefully.

Time Complexity: O(n)
Space Complexity: O(n)
"""

# Read the array from user input
a = list(map(int, input().split()))
l = len(a)

# Read the number of positions to rotate right
k = int(input("enter the k position: "))

# Handle over-rotation: rotating by l positions = no rotation
k %= l

# Split the array: left part goes up to (l-k), right part is the last k elements
rev = a[:l - k]      # Left portion of the array
rev11 = rev[::-1]    # Reverse the left portion

rev1 = a[l - k:]     # Right portion (last k elements)
rev22 = rev1[::-1]   # Reverse the right portion

# Concatenate reversed parts and reverse the whole to get right-rotated array
temp = rev11 + rev22
temp2 = temp[::-1]

# Print the right-rotated array
print(temp2)
