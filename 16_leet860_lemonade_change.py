"""
Problem: LeetCode 860 — Lemonade Change
At a lemonade stand, each lemonade costs $5. Customers pay with $5, $10, or $20 bills.
Return True if you can provide correct change to every customer, False otherwise.

Approach:
Greedy with cash tracking.
- Track the count of $5 and $10 bills (you never need to give $20 as change).
- For a $10 bill: give one $5 back.
- For a $20 bill: preferably give one $10 + one $5 (saves $5s for future use);
  if no $10, give three $5s.
- If you can't make change at any point, return False.

Time Complexity: O(n) — single pass through the bills list.
Space Complexity: O(1) — only three counters used.
"""

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        # Count of each bill denomination available for change
        five = 0
        ten = 0
        twenty = 0   # Not needed for giving change, but tracked here

        for i in bills:
            if i == 5:
                # Customer pays exactly $5 — no change needed, just collect
                five += 1

            elif i == 10:
                # Customer pays $10 — need to give $5 change
                if five > 0:
                    five -= 1
                    ten += 1
                else:
                    return False   # Can't make change

            else:
                # Customer pays $20 — need to give $15 change
                if five > 0 and ten > 0:
                    # Preferred: use one $10 + one $5 (preserves $5 bills)
                    five -= 1
                    ten -= 1
                elif five >= 3:
                    # Fallback: use three $5 bills
                    five -= 3
                else:
                    return False   # Can't make change

        # Successfully gave change to all customers
        return True
