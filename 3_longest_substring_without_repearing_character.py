class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 1:
            return len(s)

        start_idx = -1 # keep track of where curr substring start is
        max_len = 0 # output
        dict_char_idx = {} # {char: idx} curr substring's character existing index
        for i in range(len(s)):
            char = s[i]
            # if char in dict
            if (char in dict_char_idx) and (dict_char_idx[char]>start_idx):
                start_idx = dict_char_idx[char] # 3
                dict_char_idx[char] = i
            # if char not in dict
            else:
                dict_char_idx[char] = i
                if i - start_idx > max_len:
                    max_len = i - start_idx

        return max_len