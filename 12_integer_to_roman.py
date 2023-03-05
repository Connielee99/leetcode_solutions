class Solution:
    def intToRoman(self, num: int) -> str:
        
        dict_int_roman = dict(zip([1,5,10,50,100,500,1000], 'I,V,X,L,C,D,M'.split(',')))
        dict_special = dict(zip([4,9,40,90,400,900], 'IV,IX,XL,XC,CD,CM'.split(',')))
        dict_int_roman.update(dict_special)
        dict_int_roman = dict(sorted(dict_int_roman.items(), reverse=True))

        output = ''
        
        if num < 1 or num > 3999:
            return output

        for value, symbol in dict_int_roman.items():
            while num >= value:
                output += symbol
                num -= value

        return output