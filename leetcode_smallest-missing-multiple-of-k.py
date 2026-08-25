from typing import List
from itertools import count

class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        # Time Complexity: O(n + m) where m is the index of the missing multiple (at most n+1)
        # Space Complexity: O(n)
        
        # Step 1: Create hash table (set) of all numbers present in nums
        # (this effectively tracks which multiples of k are present)
        present = set(nums)
        
        # Step 2 & 3: Check multiples of k starting from smallest (k*1, k*2, ...)
        # and return the first one whose value is not in the hash table (missing)
        for i in count(1):
            multiple = k * i
            if multiple not in present:
                return multiple


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [8, 2, 3, 4, 6]
    k1 = 2
    print(f"Example 1: nums = {nums1}, k = {k1}")
    print(f"Output: {sol.missingMultiple(nums1, k1)}")  # Expected: 10
    
    # Example 2
    nums2 = [1, 4, 7, 10, 15]
    k2 = 5
    print(f"\nExample 2: nums = {nums2}, k = {k2}")
    print(f"Output: {sol.missingMultiple(nums2, k2)}")  # Expected: 5
    
    # Extra test
    nums3 = [2, 4, 6, 8, 10]
    k3 = 2
    print(f"\nExtra: nums = {nums3}, k = {k3}")
    print(f"Output: {sol.missingMultiple(nums3, k3)}")  # Expected: 12
