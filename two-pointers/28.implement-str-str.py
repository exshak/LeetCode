#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
# https://leetcode.com/problems/implement-strstr/description/
#
# algorithms
# Easy (33.69%)
# Likes:    1310
# Dislikes: 1709
# Total Accepted:    587.2K
# Total Submissions: 1.7M
# Testcase Example:  '"hello"\n"ll"'
#
# Implement strStr().
# 
# Return the index of the first occurrence of needle in haystack, or -1 if
# needle is not part of haystack.
# 
# Example 1:
# 
# 
# Input: haystack = "hello", needle = "ll"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# 
# 
# Clarification:
# 
# What should we return when needle is an empty string? This is a great
# question to ask during an interview.
# 
# For the purpose of this problem, we will return 0 when needle is an empty
# string. This is consistent to C's strstr() and Java's indexOf().
# 
#

# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
# @lc code=end
