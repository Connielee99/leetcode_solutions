class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 0: return False
        stack = []
        dict_b = {
            '(': ')',
            '[': ']',
            '{': '}'
        }
        for i in s:
            if i in dict_b:
                # left paren push
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False
                else:
                    popped = stack.pop()
                    if dict_b[popped] != i:
                        return False
        if len(stack) == 0: return True
        return False