class Solution:
    def resultArray(self, nums: list[int]) -> list[int]:
        # Time: O(n), Space: O(n)
        # Simulate the distribution process as described
        
        # First operation: append nums[0] to arr1
        arr1 = [nums[0]]
        # Second operation: append nums[1] to arr2
        arr2 = [nums[1]]
        
        # For remaining elements (from index 2 onwards)
        for i in range(2, len(nums)):
            # If last of arr1 > last of arr2, append to arr1
            if arr1[-1] > arr2[-1]:
                arr1.append(nums[i])
            else:
                # Otherwise append to arr2
                arr2.append(nums[i])
        
        # Result is concatenation of arr1 and arr2
        return arr1 + arr2


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    nums1 = [2, 1, 3]
    print("Input:", nums1)
    print("Output:", sol.resultArray(nums1))
    print("Expected: [2, 3, 1]")
    print()
    
    # Example 2
    nums2 = [5, 4, 3, 8]
    print("Input:", nums2)
    print("Output:", sol.resultArray(nums2))
    print("Expected: [5, 3, 4, 8]")
