#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 21:17:33 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3371/
Problem description: 
Find the Duplicate Number
Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

Example 1:

Input: [1,3,4,2,2]
Output: 2
Example 2:

Input: [3,1,3,4,2]
Output: 3
Note:

You must not modify the array (assume the array is read only).
You must use only constant, O(1) extra space.
Your runtime complexity should be less than O(n2).
There is only one duplicate number in the array, but it could be repeated more than once.

"""
# Full explanation: https://leetcode.com/problems/find-the-duplicate-number/solution/
# Time: O(n), space: O(1)
class Solution:
    def findDuplicate(self, nums) -> int:
        hare = tortoise = 0
        
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        tortoise = 0
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
            
        return tortoise
    
sol = Solution()

# Test 1
print(sol.findDuplicate([1,3,4,2,2]))

# Test 2
print(sol.findDuplicate([3,1,3,4,2]))
