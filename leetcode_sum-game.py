class Solution:
    def sumGame(self, num: str) -> bool:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        n = len(num)
        ans = 0.0

        def get_expectation(c: str) -> float:
            # '?' ka expected value 4.5 hai (0 se 9 tak average)
            return 4.5 if c == '?' else int(c)

        # Left half ka expected sum add karo
        for i in range(n // 2):
            ans += get_expectation(num[i])

        # Right half ka expected sum subtract karo
        for i in range(n // 2, n):
            ans -= get_expectation(num[i])

        # Agar expected difference zero nahi hai to Alice jeetegi
        return ans != 0.0


if __name__ == "__main__":
    sol = Solution()

    # Example 1
    num1 = "5023"
    print(f"Input: num = \"{num1}\"")
    print(f"Output: {sol.sumGame(num1)}")
    print("Explanation: No '?' so sums equal (5+0 == 2+3), Bob wins.\n")

    # Example 2
    num2 = "25??"
    print(f"Input: num = \"{num2}\"")
    print(f"Output: {sol.sumGame(num2)}")
    print("Explanation: Alice can force unequal sums.\n")

    # Example 3
    num3 = "?3295???"
    print(f"Input: num = \"{num3}\"")
    print(f"Output: {sol.sumGame(num3)}")
    print("Explanation: Bob can always force equal sums.")
