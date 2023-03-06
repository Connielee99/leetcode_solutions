class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        output = ''
        if len(strs) < 1:
            return output
        pointer = 0
        n_elems = len(strs)
        min_len = min([len(x) for x in strs])

        while pointer <= min_len-1:
            curr_prefix = [string[pointer] for string in strs]
            if len(set(curr_prefix)) == 1:
                output += curr_prefix[0]
                pointer += 1
            else:
                break
        return output