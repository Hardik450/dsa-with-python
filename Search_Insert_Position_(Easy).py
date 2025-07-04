"""
Search Insert Position

Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
"""


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
# I am traversing each element using for loop and checking in first condition, whether they are equal to target or not, then second condition checks when the target will become lower and in last if any of the conditions aren't met then the target will be at the total length of the list.
        for i in range(len(nums)):
            if target == nums[i]:
                return i
            elif (target < nums[i]):
                return i
        return len(nums)
