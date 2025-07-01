"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

"""

class Solution:
    def isPalindrome(self, x: int) -> bool:
# Here, a is the reversed number to which we're initializing as 0 and storing original number in b.
        a = 0
        b = x
# Number equals to or less than 0 ain't palindrome number.
        if x < 0:
            return False
# The loop takes input and assign 'a' with the sum of the remainder of the number and the product of 10 and a. Then, we will reduce x until it equals to zero.
        while x > 0:
            a = (x % 10) + (a * 10)
            x = x // 10
        print(a)
        return a == b

        # Time Complexity is O(logN)
        # Space Complexity is O(1)
