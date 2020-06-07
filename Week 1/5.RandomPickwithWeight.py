#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 21:40:02 2020

@author: nenad
"""


"""


"""
from random import randint
from bisect import bisect_left
class Solution:
    def __init__(self, w):
        self.buckets = []
        self._populateSpace(w)
    def _populateSpace(self, w):
        cumsum = 0
        for val in w:
            prev = cumsum
            cumsum += val
            self.buckets.append([prev, cumsum])
    def _binSearch(self, arr, low, high, val):
        if low > high:
            return -1
        mid = low + (high-low)//2
        left, right = arr[mid]
        if left < val <= right:
            return mid
        if val <= left:
            return self._binSearch(arr, low, mid-1, val)
        else:
            return self._binSearch(arr, mid+1, high, val)

    def pickIndex(self) -> int:
        cumsum = self.buckets[-1][-1]
        val = randint(1, cumsum)
        # do this task again with bisect functions from bisect lib
        return self._binSearch(self.buckets, 0, len(self.buckets)-1, val)
                
# Test 1    
w = [1]    
sol = Solution(w)
print(sol.pickIndex())

# Test 2
w = [1,3]    
sol = Solution(w)
for i in range(5):
    print(sol.pickIndex())