# 74. Search a 2D Matrix

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/search-a-2d-matrix/

**Topics:** Array, Binary Search, Matrix

## Problem

You are given an `m x n` integer matrix `matrix` with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.

Given an integer `target`, return `true` *if* `target` *is in* `matrix` *or* `false` *otherwise*.

You must write a solution in `O(log(m * n))` time complexity.

**Example 1:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
```
**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
**Output:** true
```

**Example 2:**

![](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)
```
**Input:** matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
**Output:** false
```

**Constraints:**

- `m == matrix.length`
- `n == matrix[i].length`
- `1 <= m, n <= 100`
- `-10^4 <= matrix[i][j], target <= 10^4`

## Solution (python3)

```py
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        left=0
        right=rows*cols-1
        while left<=right:
            mid=(left+right)//2
            row=mid//cols
            col=mid%cols
            value=matrix[row][col]
            if value==target:
                return True
            elif value<target:
                left=mid+1
            else:
                right=mid-1
        return False
        
```

*Runtime: 0 ms · Memory: 19.6 MB*

