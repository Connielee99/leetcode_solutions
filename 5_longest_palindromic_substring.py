class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_start, max_len = 0, 1
        for i in range(len(s)):
            # max_len += 2 in order to make it odd
            # odd starts at 3, always bigger than even, so we start by checking if it's an odd
            odd_start, even_start = i - 1 - max_len, i - max_len
            odd_str, even_str = s[odd_start:(i+1)], s[even_start:(i+1)]
            if (odd_start >= 0) and (odd_str == odd_str[::-1]):
                max_start = odd_start
                max_len += 2
            elif (even_start >= 0) and (even_str == even_str[::-1]):
                max_start = even_start
                max_len += 1
        return s[max_start:(max_start+max_len)]