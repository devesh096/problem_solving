from typing import List
from collections import defaultdict

class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        # Time: O(m) where m = len(reservedSeats)
        # Space: O(m)
        
        # Map: row -> set of reserved seats in that row
        reserved = defaultdict(set)
        for row, seat in reservedSeats:
            reserved[row].add(seat)
        
        ans = 0
        
        # Process only rows that have reservations
        for seats in reserved.values():
            left = 2 not in seats and 3 not in seats and 4 not in seats and 5 not in seats
            middle = 4 not in seats and 5 not in seats and 6 not in seats and 7 not in seats
            right = 6 not in seats and 7 not in seats and 8 not in seats and 9 not in seats
            
            if left and right:
                ans += 2
            elif left or middle or right:
                ans += 1
            # else 0
        
        # Empty rows (no reservations) can always take 2 groups
        empty_rows = n - len(reserved)
        ans += empty_rows * 2
        
        return ans


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 3
    reserved1 = [[1,2],[1,3],[1,8],[2,6],[3,1],[3,10]]
    print("Example 1:", sol.maxNumberOfFamilies(n1, reserved1))  # Expected: 4
    
    # Example 2
    n2 = 2
    reserved2 = [[2,1],[1,8],[2,6]]
    print("Example 2:", sol.maxNumberOfFamilies(n2, reserved2))  # Expected: 2
    
    # Example 3
    n3 = 4
    reserved3 = [[4,3],[1,4],[4,6],[1,7]]
    print("Example 3:", sol.maxNumberOfFamilies(n3, reserved3))  # Expected: 4
