class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        left = 0
        ans = 0
        seen = {}

        # seen {
        #   a : 1
        #   b : 2
        #   c : 3
        # }

        for right, char in enumerate(s):
            if char in seen and left <= seen[char]:
                left = seen[char] + 1
            seen[char] = right
            ans = max(ans, right - left + 1)
        return ans