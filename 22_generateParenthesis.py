class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        output = []

        def dfs_recursion(left: int, right: int, curr_output: str):
            # base case: well-formed parentheses
            if n == left == right:
                output.append(curr_output)
                return
            if left < n:
                dfs_recursion(left+1, right, curr_output+'(')
            if right < left:
                dfs_recursion(left, right+1, curr_output+')')
        
        dfs_recursion(0, 0, '')


        return output