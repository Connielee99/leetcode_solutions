class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_digit_letter = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        
        # 23
        #   a       b
        # d e f  d  e  f

        output = []

        def helper_backtrack(index, curr_str):
            if len(curr_str) == len(digits):
                output.append(curr_str)
                return
            for char in dict_digit_letter[digits[index]]:
                helper_backtrack(index+1, curr_str+char)
            return
        
        if digits:
            helper_backtrack(0, '')

        return output