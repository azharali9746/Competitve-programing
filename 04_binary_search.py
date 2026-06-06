"""
Problem:
Given a list of integers and a target value k, find the index of k in the
sorted array using Binary Search. Print the index if found, or -1 if not.

Approach:
Binary Search.
- Sort the array first.
- Use two pointers (low and high) to narrow down the search range.
- At each step, check the middle element:
    - If it equals k, store the index and stop.
    - If k is smaller, search the left half.
    - If k is larger, search the right half.

Time Complexity: O(n log n) — O(n log n) for sorting + O(log n) for search.
Space Complexity: O(1) — search done in-place.
"""

# Read the list of integers from user input
arr = list(map(int, input().split()))

# Read the target value to search for
k = int(input())

# Sort the array — required for binary search to work correctly
arr.sort()

# Initialize the two boundary pointers and result index
low, high = 0, len(arr) - 1
idx = -1   # Default: -1 means element not found

# Binary search loop — continue while search range is valid
while low <= high:
    # Find the middle index to avoid overflow (safe integer midpoint)
    mid = (low + high) // 2

    if k == arr[mid]:
        # Target found at mid — save index and stop
        idx = mid
        break
    elif k < arr[mid]:
        # Target is in the left half — discard right half
        high = mid - 1
    else:
        # Target is in the right half — discard left half
        low = mid + 1

# Print the index of the target element (-1 if not found)
print(idx)
