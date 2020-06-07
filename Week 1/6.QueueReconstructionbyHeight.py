#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 22:39:10 2020

@author: nenad
"""


"""

Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/539/week-1-june-1st-june-7th/3352/
Problem description: 
Queue Reconstruction by Height
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

 
Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
 

   Hide Hint #1  
What can you say about the position of the shortest person?
If the position of the shortest person is i, how many people would be in front of the shortest person?
   Hide Hint #2  
Once you fix the position of the shortest person, what can you say about the position of the second shortest person?
"""
class Solution:
    def reconstructQueue(self, people):
        n = len(people)
        people.sort()        
        queue = [None] * n
        for person in people:
            height, pos = person
            count = pos
            for i in range(n):
                if count == 0:
                    queue[i] = person
                    break
                if queue[i] is not None:
                    count -= 1
            
        return queue
            
sol = Solution()

# Test 1
people = [[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]
print(sol.reconstructQueue(people))
        