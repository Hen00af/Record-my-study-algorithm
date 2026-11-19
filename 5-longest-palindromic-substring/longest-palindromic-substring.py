class Solution(object):
    def longestPalindrome(self, s):
        ans = ""

        for pivot in range(len(s)):
            for left, right in [(pivot, pivot), (pivot, pivot + 1)]:

                while left >= 0 and right < len(s) and s[left] == s[right]:

                    if right - left + 1 > len(ans):
                        ans = s[left:right + 1]

                    left -= 1
                    right += 1

        return ans