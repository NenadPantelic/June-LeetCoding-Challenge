#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 21:55:28 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3365/
Problem description: 
Longest Duplicate Substring
Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"
Example 2:

Input: "abcd"
Output: ""
 

Note:

2 <= S.length <= 10^5
S consists of lowercase English letters.
   Hide Hint #1  
Binary search for the length of the answer. (If there's an answer of length 10, then there are answers of length 9, 8, 7, ...)
   Hide Hint #2  
To check whether an answer of length K exists, we can use Rabin-Karp 's algorithm.

"""
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        longestString = ""
        low =0
        high =len(S)-1
        while low <= high:
            mid =low+(high-low)//2
            duplicate = self.findDuplicate(mid,S)
            if duplicate =="":
                high=mid-1
            else:
                low=mid+1
                longestString=duplicate
            
        
        return longestString
    
    def findDuplicate(self, length, string):
        substrSet = set()
        n = len(string)
        for i in range(n-length+1):
            if string[i:i+length] not in substrSet:
                substrSet.add(string[i:i+length])
            else:
                return string[i:i+length]
        
        return ""
    
sol = Solution()

# Test 1
string = "banana"
print(sol.longestDupSubstring(string))



# Test 2
string = "abcd"
print(sol.longestDupSubstring(string))