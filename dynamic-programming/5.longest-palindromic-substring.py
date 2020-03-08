#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (28.69%)
# Likes:    5646
# Dislikes: 474
# Total Accepted:    816.6K
# Total Submissions: 2.8M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
# 
# Example 1:
# 
# 
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: "cbbd"
# Output: "bb"
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        for i in range(len(s)):        
            odd = self.palindromeAt(s, i, i)
            even = self.palindromeAt(s, i, i+1)
            res = max(res, odd, even, key=len)
        return res

    # starting at l,r expand outwards to find the biggest palindrome
    def palindromeAt(self, s, l, r):    
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
        
# Time complexity : O(n^2)
# Space complexity : O(1)

# @lc code=end
