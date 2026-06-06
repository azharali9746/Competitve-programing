"""
Problem:
Given an array and a window size k, find the maximum sum of any contiguous
subarray of exactly k elements.

Approach:
Sliding Window (Optimized).
- Compute the sum of the first window of size k.
- Slide the window one step at a time: subtract the element going out (left)
  and add the element coming in (right).
- Track the maximum sum seen across all windows.

Note: The original code had syntax errors (wrong slice in range, wrong variable
names). The logic below preserves the intended sliding window approach,
with fixes applied for correctness.

Time Complexity: O(n) — single pass after initial window sum.
Space Complexity: O(1)
"""

# Read the array from user input
l = list(map(int, input().split()))

# Read the window size
k = int(input("position: "))
l1 = len(l)

# Compute the sum of the first window of size k
s = sum(l[:k])

# Initialize the maximum sum with the first window's sum
m = s

# Slide the window from index 1 to (l1 - k)
for i in range(1, l1 - k + 1):
    # Slide: remove the element that just left the window (l[i-1])
    #        add the new element that entered the window (l[i+k-1])
    s = s - l[i - 1] + l[i + k - 1]

    # Update maximum if new window sum is greater
    m = max(m, s)

# Print the maximum sum of any window of size k
print(m)
