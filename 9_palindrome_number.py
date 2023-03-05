class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: return False
        if x < 10: return True
        # convert to string
        string = str(x)
        return string == string[::-1]
        """
        even = True if len(string) % 2 == 0 else False
        if even:
            left, right = len(string)//2-1, len(string)//2
        else:
            left, right = len(string)//2-1, len(string)//2+1
        while (left>=0 and right <=len(string)):
            if string[left] != string[right]: 
                return False
            else:
                left -=1
                right += 1
        return True
        """