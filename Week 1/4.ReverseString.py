#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 20:34:40 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3350/
Problem description: 
Reverse String
Write a function that reverses a string. The input string is given as an array of characters char[].

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

You may assume all the characters consist of printable ascii characters.

 

Example 1:

Input: ["h","e","l","l","o"]
Output: ["o","l","l","e","h"]
Example 2:

Input: ["H","a","n","n","a","h"]
Output: ["h","a","n","n","a","H"]

The entire logic for reversing a string is based on using the opposite directional two-pointer approach!

"""

class Solution:
    def reverseString(self, s) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n = len(s)
        for i in range(n//2):
            s[i], s[n-i-1] = s[n-i-1], s[i]
    
    
sol = Solution()

# Test 1
s = ["h","e","l","l","o"]
sol.reverseString(s)
print(s)


# Test 2
s = ["H","a","n","n","a","h"]
sol.reverseString(s)
print(s)
      