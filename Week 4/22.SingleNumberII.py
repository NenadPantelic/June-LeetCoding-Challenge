#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 22 21:16:09 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/542/week-4-june-22nd-june-28th/3368/
Problem description: 
Single Number II
Given a non-empty array of integers, every element appears three times except for one, which appears exactly once. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,3,2]
Output: 3
Example 2:

Input: [0,1,0,1,0,1,99]
Output: 99
"""
from collections import Counter
class Solution:
    def singleNumber(self, nums) -> int:
        counter = Counter(nums)
        for val in counter:
            if counter[val] == 1:
                return val
            
            
sol = Solution()

# Test 1
inp = [2,2,3,2]
print(sol.singleNumber(inp))

# Test 2
inp = [0,1,0,1,0,1,99]
print(sol.singleNumber(inp))