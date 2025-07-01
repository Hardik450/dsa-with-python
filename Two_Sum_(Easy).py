"""Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
"""


"""
Method 1:-
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
# First, i will try to traverse each element in the list
        for i in range(len(nums)):
# This loop is setup so that i can traverse other elements except the one which we're traversing in first loop and check the sum of 2 elements (one which we're traversing in first loop and second which we're traversing in second loop) equals to the target or not. 
            for j in range(i + 1, len(nums)):
# Condition to check the sum
                if nums[i] + nums[j] == target:
                    return [i, j]
"""
# Method 2 (more optimize)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[num] = i
