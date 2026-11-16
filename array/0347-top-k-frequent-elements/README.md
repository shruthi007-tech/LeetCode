# 347. Top K Frequent Elements

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/top-k-frequent-elements/

**Topics:** Array, Hash Table, Divide and Conquer, Sorting, Heap (Priority Queue), Bucket Sort, Counting, Quickselect

## Problem

Given an integer array `nums` and an integer `k`, return *the* `k` *most frequent elements*. You may return the answer in **any order**.

**Example 1:**

**Input:** nums = [1,1,1,2,2,3], k = 2

**Output:** [1,2]

**Example 2:**

**Input:** nums = [1], k = 1

**Output:** [1]

**Example 3:**

**Input:** nums = [1,2,1,2,1,2,3,1,3,2], k = 2

**Output:** [1,2]

**Constraints:**

- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i] <= 10^4`
- `k` is in the range `[1, the number of unique elements in the array]`.
- It is **guaranteed** that the answer is **unique**.

**Follow up:** Your algorithm's time complexity must be better than `O(n log n)`, where n is the array's size.

## Solution (python3)

```py
class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

            sorted_nums = sorted(count, key=count.get, reverse=True)

        return sorted_nums[:k]
        
```

*Runtime: 6645 ms · Memory: 22.5 MB*

