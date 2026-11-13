# 49. Group Anagrams

**Difficulty:** Medium

**Link:** https://leetcode.com/problems/group-anagrams/

**Topics:** Array, Hash Table, String, Sorting

## Problem

Given an array of strings `strs`, group the anagrams together. You can return the answer in **any order**.

**Example 1:**

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]

**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]

**Explanation:**

- There is no string in strs that can be rearranged to form `"bat"`.
- The strings `"nat"` and `"tan"` are anagrams as they can be rearranged to form each other.
- The strings `"ate"`, `"eat"`, and `"tea"` are anagrams as they can be rearranged to form each other.

**Example 2:**

**Input:** strs = [""]

**Output:** [[""]]

**Example 3:**

**Input:** strs = ["a"]

**Output:** [["a"]]

**Constraints:**

- `1 <= strs.length <= 10^4`
- `0 <= strs[i].length <= 100`
- `strs[i]` consists of lowercase English letters.

## Solution (python3)

```py
class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        groups={}
        for word in strs:
            key=" ".join(sorted(word))
            if key not in groups:
                groups[key]=[]
            groups[key].append(word)
        return list(groups.values())

        
```

*Runtime: 13 ms · Memory: 21.8 MB*

