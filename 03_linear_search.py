"""
Problem:
Given a list of integers and a target value k, determine whether k exists
in the list. Print "yes" if found, "no" otherwise.

Approach:
Linear Search.
- Iterate through each element one by one.
- If a match is found, print "yes" and stop immediately (break).
- If the loop completes without finding k, the for-else prints "no".

Time Complexity: O(n) — in the worst case, all elements are checked.
Space Complexity: O(1) — no extra space used.
"""

# Read the list of integers from user input
l = list(map(int, input().split()))

# Read the target value to search for
k = int(input())

# Iterate through each element in the list
for i in l:
    if i == k:
        # Target found — print result and exit the loop early
        print("yes")
        break
else:
    # This block runs only if the loop completed without a break (not found)
    print("no")
