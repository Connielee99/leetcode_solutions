class Solution:
    def intToRoman(self, num: int) -> str:
        
        dict_int_roman = {1000: 'M', 900: 'CM', 500: 'D', 400: 'CD', 100: 'C', 90: 'XC', 50: 'L', 40: 'XL', 10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'}

        output = ''
        
        if num < 1 or num > 3999:
            return output

        for value, symbol in dict_int_roman.items():
            while num >= value:
                output += symbol
                num -= value

        return output