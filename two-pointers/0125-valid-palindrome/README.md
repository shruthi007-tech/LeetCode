# 125. Valid Palindrome

**Difficulty:** Easy

**Link:** https://leetcode.com/problems/valid-palindrome/

**Topics:** Two Pointers, String

## Problem

A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `true`* if it is a **palindrome**, or *`false`* otherwise*.

**Example 1:**

```
**Input:** s = "A man, a plan, a canal: Panama"
**Output:** true
**Explanation:** "amanaplanacanalpanama" is a palindrome.
```

**Example 2:**

```
**Input:** s = "race a car"
**Output:** false
**Explanation:** "raceacar" is not a palindrome.
```

**Example 3:**

```
**Input:** s = " "
**Output:** true
**Explanation:** s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.
```

**Constraints:**

- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

## Solution (python3)

```py
class Solution:
    def isPalindrome(self, s: str) -> bool:
        new = ""

        for ch in s:
            if ch.isalnum():
                new += ch.lower()

        rev = new[::-1]

        return new == rev
```

*Runtime: 8 ms · Memory: 19.4 MB*

