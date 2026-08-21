from typing import List
from math import lcm
from bisect import bisect_left

class Solution:
    def findKthSmallest(self, coins: List[int], k: int) -> int:
        # Time: O(n * 2^n * log(MAX)) where n <= 15, MAX ~ 1e11
        # Space: O(1) extra (besides input)
        
        def check(mx: int) -> bool:
            """Count how many distinct amounts <= mx can be formed.
            Uses inclusion-exclusion over all non-empty subsets of coins.
            """
            cnt = 0
            n = len(coins)
            for i in range(1, 1 << n):  # all non-empty subsets via bitmask
                v = 1
                for j, x in enumerate(coins):
                    if i >> j & 1:
                        v = lcm(v, x)
                        if v > mx:
                            break  # further LCM only larger; mx//v will be 0
                m = i.bit_count()  # number of coins in this subset
                if m & 1:  # odd size -> add
                    cnt += mx // v
                else:      # even size -> subtract
                    cnt -= mx // v
            return cnt >= k
        
        # Binary search the smallest amount x such that count(x) >= k
        # Upper bound is safe: k * min(coins) <= 2e9 * 25 = 5e10
        return bisect_left(range(10**11), True, key=check)


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    coins1 = [3, 6, 9]
    k1 = 3
    print(f"Input: coins = {coins1}, k = {k1}")
    print(f"Output: {sol.findKthSmallest(coins1, k1)}")  # Expected: 9
    
    # Example 2
    coins2 = [5, 2]
    k2 = 7
    print(f"\nInput: coins = {coins2}, k = {k2}")
    print(f"Output: {sol.findKthSmallest(coins2, k2)}")  # Expected: 12
    
    # Extra test
    coins3 = [1]
    k3 = 5
    print(f"\nInput: coins = {coins3}, k = {k3}")
    print(f"Output: {sol.findKthSmallest(coins3, k3)}")  # Expected: 5
