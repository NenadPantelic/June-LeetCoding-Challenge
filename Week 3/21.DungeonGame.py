#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 20:49:10 2020

@author: nenad
"""


"""
Problem URL: https://leetcode.com/explore/challenge/card/june-leetcoding-challenge/541/week-3-june-15th-june-21st/3367/
Problem description: 
Dungeon Game
The demons had captured the princess (P) and imprisoned her in the bottom-right corner of a dungeon. The dungeon consists of M x N rooms laid out in a 2D grid. Our valiant knight (K) was initially positioned in the top-left room and must fight his way through the dungeon to rescue the princess.

The knight has an initial health point represented by a positive integer. If at any point his health point drops to 0 or below, he dies immediately.

Some of the rooms are guarded by demons, so the knight loses health (negative integers) upon entering these rooms; other rooms are either empty (0's) or contain magic orbs that increase the knight's health (positive integers).

In order to reach the princess as quickly as possible, the knight decides to move only rightward or downward in each step.

 

Write a function to determine the knight's minimum initial health so that he is able to rescue the princess.

For example, given the dungeon below, the initial health of the knight must be at least 7 if he follows the optimal path RIGHT-> RIGHT -> DOWN -> DOWN.

-2 (K)	-3	3
-5	-10	1
10	30	-5 (P)
 

Note:

The knight's health has no upper bound.
Any room can contain threats or power-ups, even the first room the knight enters and the bottom-right room where the princess is imprisoned.

"""
class Solution:
    def __init__(self):
        self.bestPathValue = float("-inf")
    def isSafe(self, x, y, m, n, visited):
        return 0 <= x < m and 0 <= y < n and not visited[x][y]
    
    
    def calculateMinimumHP(self, dungeon) -> int:
        m = len(dungeon)
        if m == 0:
            return 1
        n = len(dungeon[0])
        if n == 0:
            return 1
        visited = [[False for j in range(n)] for i in range(m)]
        self.findThePath(dungeon, 0, 0, m, n, visited, 0, float("inf"))
        optimalPathCost = self.bestPathValue        
        return 1 if optimalPathCost >= 0 else -optimalPathCost + 1
        
    def findThePath(self, dungeon, x, y, m, n, visited, pathSum, maxLostPointsOnThisRoute):
        if x == m-1 and y == n-1:
            pathSum += dungeon[x][y]
            maxLostPointsOnThisRoute = min(maxLostPointsOnThisRoute, pathSum)
            self.bestPathValue = max(self.bestPathValue, maxLostPointsOnThisRoute)
            return
        if self.isSafe(x, y, m, n, visited):
            visited[x][y] = True
            pathSum += dungeon[x][y]
            maxLostPointsOnThisRoute = min(maxLostPointsOnThisRoute, pathSum)
            self.findThePath(dungeon, x+1, y, m, n, visited, pathSum, maxLostPointsOnThisRoute)
            self.findThePath(dungeon, x, y+1, m, n, visited, pathSum, maxLostPointsOnThisRoute)
            visited[x][y] = False
        
sol = Solution()

# Test 1

dungeon = [[-2, -3,    3],
[-5,    -10,    1],
[10,    30,    -5]]
print(sol.calculateMinimumHP(dungeon))
                                           
# Test 2
dungeon = [[2],[1]]                                                                                                 
print(sol.calculateMinimumHP(dungeon))
