"""
Plus One

You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
"""



class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = 1
        # I am incrementing the last element with 1 but if the element is 9 then it will become 10 so i will leave 0 on the place of 9 and carry of 1 will go to next element.
        for i in range(len(digits)-1, -1, -1):
            digits[i] = digits[i] + x
            print(digits[i])
            x = digits[i] // 10
            digits[i] = digits[i] % 10
# Below condition is put up because if the list is [9,9,9,9] then it will become [0,0,0,0] by using above loop and x will have carry 1 so to make the list look like this [1,0,0,0,0] we will use below condition.
        if x:
            result = [0] * (len(digits) + 1)
            result[0] = 1
            for i in range(1, len(digits)+1):
                result[i] = digits[i-1]
            return result
        return digits
