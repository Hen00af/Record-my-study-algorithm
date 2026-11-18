class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ans = 0
        seen = {}

        # s = "abcabcbb"
        # 1.
        # right = 0
        # left = 0
        # seen = {}
        # char = `a`

        for right, char in enumerate(s):
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            # seen = { `a` : 0 }
            seen[char] = right
            ans = max(ans, right - left + 1)

        return ans
