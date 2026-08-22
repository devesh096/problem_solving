class Solution:
    def checkDivisibility(self, n: int) -> bool:
        # Time Complexity: O(log n) - number of digits
        # Space Complexity: O(1)
        original = n
        digit_sum = 0
        digit_product = 1
        
        while n > 0:
            digit = n % 10
            digit_sum += digit
            digit_product *= digit
            n //= 10
        
        total = digit_sum + digit_product
        return original % total == 0


if __name__ == "__main__":
    sol = Solution()
    
    # Example 1
    n1 = 99
    print(f"Input: n = {n1}")
    print(f"Output: {sol.checkDivisibility(n1)}")
    print("Expected: True")
    print()
    
    # Example 2
    n2 = 23
    print(f"Input: n = {n2}")
    print(f"Output: {sol.checkDivisibility(n2)}")
    print("Expected: False")
    print()
    
    # Extra test: number with zero
    n3 = 10
    print(f"Input: n = {n3}")
    print(f"Output: {sol.checkDivisibility(n3)}")
    # sum=1, prod=0, total=1, 10%1==0 -> True
    print("Expected: True")
