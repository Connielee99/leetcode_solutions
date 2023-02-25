class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if len(s) <= 1:
            return len(s)

        dict_char_idx = {}
        max_len = 0
        start_idx = -1

        for i in range(len(s)):
            char = s[i] # a
            # char in dict
            if (char in dict_char_idx) and (dict_char_idx[char] > start_idx):
                start_idx = dict_char_idx[char] 
                dict_char_idx[char] = i 

            # char not in dict
            else:
                dict_char_idx[char] = i
                if max_len < i - start_idx:
                    max_len = i - start_idx #3

        return max_len
        