"""
Problem:
Given an array and a value k, rotate the array to the LEFT by k positions.
Example: [1,2,3,4,5], k=2  →  [3,4,5,1,2]

Approach:
Reversal Algorithm.
Step 1: Split array into two parts at index k.
Step 2: Reverse the first part (indices 0 to k-1).
Step 3: Reverse the second part (indices k to end).
Step 4: Concatenate both reversed parts.
Step 5: Reverse the entire concatenated array.
Result: The array is left-rotated by k positions.

Intuition: Reversing parts and then the whole "unscrambles" the rotation.

Time Complexity: O(n) — each element is touched a constant number of times.
Space Complexity: O(n) — new lists are created for the reversed parts.
"""

# Read the array from user input
a = list(map(int, input().split()))

# Read the number of positions to rotate left
k = int(input("enter the k rotation: "))

# Step 1: Split the array at index k
# Left part: elements from index 0 to k-1
# Right part: elements from index k to end
rev = a[k:]        # Right part of the split
rev11 = rev[::-1]  # Reverse the right part

rev1 = a[:k]        # Left part of the split
rev22 = rev1[::-1]  # Reverse the left part

# Step 2: Concatenate the two reversed parts
temp = rev11 + rev22

# Step 3: Reverse the entire joined array to get the final rotated result
temp2 = temp[::-1]

# Print the left-rotated array
print(temp2)
