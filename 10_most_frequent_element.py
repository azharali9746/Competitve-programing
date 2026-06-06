"""
Problem:
Given an array of integers, find the element that appears the most frequently
and print its frequency and value.

Approach:
Hash Map (Frequency Count).
- Use a dictionary to count occurrences of each element.
- Find the maximum frequency using max().
- Scan the original array again to find the first element with that max frequency
  (preserves original order for tie-breaking).

Time Complexity: O(n) — two passes through the array.
Space Complexity: O(n) — dictionary stores up to n unique elements.
"""

# Read the array from user input
a = list(map(int, input().split()))

# Build a frequency map: key = element, value = count
freq = {}
for i in a:
    if i in freq:
        freq[i] += 1   # Increment count if already seen
    else:
        freq[i] = 1    # First occurrence

# Find the maximum frequency value across all elements
b = max(freq.values())

# Find the element in the original array that has the max frequency
# (scanning original array preserves insertion-order tie-breaking)
max1 = 0   # Tracks current maximum frequency during scan
ele = 0    # Tracks the element with max frequency

for i in a:
    if freq[i] > max1:
        max1 = freq[i]
        ele = i

# Print: maximum frequency and the corresponding element
print(max1, ele)
