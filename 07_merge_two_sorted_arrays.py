"""
Problem:
Given two sorted arrays l1 and l2, merge them into a single sorted array.

Approach:
Two Pointers (Merge step of Merge Sort).
- Use two pointers i and j starting at the beginning of each array.
- Compare elements at i and j: append the smaller one and advance that pointer.
- After one array is exhausted, append the remaining elements of the other.

Time Complexity: O(n + m) — where n and m are the lengths of l1 and l2.
Space Complexity: O(n + m) — for the result array.
"""

# Read the two sorted arrays from user input
l1 = list(map(int, input().split()))
l2 = list(map(int, input().split()))

# Result array to hold the merged output
res = []

# Initialize two pointers, one for each array
i, j = 0, 0

# Compare elements from both arrays and append the smaller one
while i < len(l1) and j < len(l2):
    if l1[i] < l2[j]:
        res.append(l1[i])
        i += 1   # Advance pointer in l1
    else:
        res.append(l2[j])
        j += 1   # Advance pointer in l2

# If l1 still has remaining elements, append them all
while i < len(l1):
    res.append(l1[i])
    i += 1

# If l2 still has remaining elements, append them all
while j < len(l2):
    res.append(l2[j])
    j += 1

# Print the merged sorted array
print(res)
