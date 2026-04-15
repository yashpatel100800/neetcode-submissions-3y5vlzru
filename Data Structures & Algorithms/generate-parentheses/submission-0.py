class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        output = []
        stack = []

        def back(o,c):
            if o == n and c == n:
                output.append("".join(stack))

            if(o<n):
                stack.append("(")
                back(o+1,c)
                stack.pop()
            if(o>c):
                stack.append(")")
                back(o,c+1)
                stack.pop()

        back(0,0)
        return output
            
        