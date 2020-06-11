#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 23:15:12 2020

@author: nenad
"""
"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/540/week-2-june-8th-june-14th/3356/
Problem description: 

Search Insert Position
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0
"""

import bisect
class Solution:
    def searchInsert(self, nums, target: int) -> int:
        return bisect.bisect_left(nums, target)
    
sol  = Solution()

# Test 1
nums = [1,3,5,6]; target = 5
print(sol.searchInsert(nums, target))

# Test 2
nums = [1,3,5,6]; target = 2
print(sol.searchInsert(nums, target))


# Test 3
nums = [1,3,5,6]; target = 7
print(sol.searchInsert(nums, target))

# Test 4
nums = [1,3,5,6]; target = 0
print(sol.searchInsert(nums, target))