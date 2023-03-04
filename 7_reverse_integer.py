class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) < 10: return x
        string = str(x)
        neg = False
        if string[0] == '-':
            neg = True
            string = string[1:]
        if string[-1] == '0':
            string = string[:-1]
        output = int(string[::-1]) if neg == False else -1*int(string[::-1])
        if (output >= 2**31 -1) or (output <= -2**31): output = 0
        return output
            