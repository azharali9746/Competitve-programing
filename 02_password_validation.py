"""
Problem:
Validate a password based on the following rules:
  - Minimum 8 characters long
  - Must contain at least one uppercase letter
  - Must contain at least one lowercase letter
  - Must contain at least one digit
  - Must contain at least one special character
  - Must NOT contain any spaces

Approach:
Linear scan using boolean flags.
- Iterate through each character of the password.
- Set the corresponding flag (upper, lower, digit, special) when found.
- Check all conditions at the end and print "valid" or "invalid".

Time Complexity: O(n) — single pass through the password string.
Space Complexity: O(1) — only boolean flags used.
"""

# Read password input from user
n = input("enter the password:")

# Initialize flags for each character category
upper = False    # Has at least one uppercase letter
lower = False    # Has at least one lowercase letter
digit = False    # Has at least one digit
special = False  # Has at least one special character
space = False    # Has any space (not allowed)

# Scan each character in the password and set flags
for ch in n:
    if ch.isdigit():
        digit = True
    if ch.isupper():
        upper = True
    if ch.islower():
        lower = True
    if ch.isspace():
        space = True
    else:
        # Any non-space character that isn't alpha/digit counts as special
        special = True

# Check all conditions: length >= 8, all required types present, no spaces
if len(n) >= 8 and lower and digit and upper and special and not space:
    print("valid")
else:
    print("invalid")
