"""
Problem:
Given an array and a window size k, find the maximum sum of any contiguous
subarray of exactly k elements.

Approach:
Brute Force (Nested Loops).
- For every starting index i, sum the next k elements using an inner loop.
- Track the maximum sum across all windows.

Time Complexity: O(n * k) — outer loop runs (n-k) times, inner runs k times.
Space Complexity: O(1)

Note: This is the brute force approach. See the sliding window version for O(n).
"""

# Read the array from user input
l = list(map(int, input().split()))

# Read the window size k
k = int(input("position: "))

# Initialize current window sum and maximum sum found
sum1 = 0
max1 = 0

# Outer loop: try each valid starting position for a window of size k
for i in range(len(l) - k):
    # Inner loop: sum k consecutive elements starting at index i
    for j in range(i, i + k):
        sum1 += l[j]

    # Update the maximum if current window sum is greater
    if sum1 > max1:
        max1 = sum1

    # Reset the current sum for the next window
    sum1 = 0

# Print the maximum sum found
print(max1)
