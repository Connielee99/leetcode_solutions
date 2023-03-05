class Solution:
    def romanToInt(self, s: str) -> int:
        
        dict_roman_int = {'M': 1000, 'CM': 900, 'D': 500, 'CD': 400, 'C': 100, 'XC': 90, 'L': 50, 'XL': 40, 'X': 10, 'IX': 9, 'V': 5, 'IV': 4, 'I': 1}
        
        output = 0
        i = 0

        while i < len(s):
            j = i+1
            if j < len(s) and s[i]+s[j] in dict_roman_int:
                output += dict_roman_int[s[i]+s[j]]
                i += 2
            else:
                output += dict_roman_int[s[i]]
                i += 1

        return output