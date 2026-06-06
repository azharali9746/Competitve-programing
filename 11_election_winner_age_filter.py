"""
Problem:
Given n voters, each with a vote (candidate ID) and an age, find the winning
candidate. Only votes from voters aged 18 or above are valid.
- If there is a unique winner, print the frequency dictionary.
- If two or more candidates are tied for the maximum votes, print -1.

Approach:
Hash Map with conditional counting.
- Iterate through votes and corresponding ages simultaneously.
- Only count a vote if the voter's age >= 18.
- Find the maximum vote count and check for ties.

Time Complexity: O(n) — single pass through voters.
Space Complexity: O(c) — where c is the number of unique candidates.
"""

# Read the number of voters
n = int(input())

# Read candidate votes (one per voter)
vote = list(map(int, input().split()))

# Read corresponding voter ages
age = list(map(int, input().split()))

# Frequency map for valid votes: key = candidate ID, value = vote count
freq = {}

# Index to track current voter's age
h = 0

for i in vote:
    if i not in freq:
        # First vote for this candidate — only add if voter is eligible
        if age[h] >= 18:
            freq[i] = 1
    else:
        # Candidate already has votes — add if voter is eligible
        if age[h] >= 18:
            freq[i] += 1
    h += 1   # Move to the next voter's age

# Find the maximum number of votes received by any candidate
mx = max(freq.values())

# Count how many candidates share the maximum vote count (tie check)
count = 0
for j in freq.values():
    if mx == j:
        count += 1

# If more than one candidate has the max votes, it's a tie → print -1
if count > 1:
    print(-1)
else:
    # Unique winner exists — print the full vote frequency dictionary
    print(freq)
