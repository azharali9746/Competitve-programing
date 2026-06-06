"""
Problem:
Given an array and an integer n, left-rotate the array by 1 position, n times.
Example: [1,2,3,4,5], n=2 → [3,4,5,1,2]

Approach:
Simulation (Brute Force).
- Repeat n times: save the first element, shift all others one step left,
  place the saved element at the end.

Time Complexity: O(n * l) — n rotations, each taking O(l) shifts.
Space Complexity: O(1) — only one temp variable.

Note: For large n, use slicing: a = a[n%l:] + a[:n%l] for O(l) time.
"""

# Read the array from user input
a = list(map(int, input().split()))

# Read how many times to left-rotate by 1
n = int(input())

# Perform n single-step left rotations
for i in range(n):
    # Save the first element before shifting
    temp = a[0]

    # Shift every element one position to the left
    for j in range(len(a) - 1):
        a[j] = a[j + 1]

    # Place the saved first element at the last position
    a[len(a) - 1] = temp

# Print the left-rotated array
print(a)
