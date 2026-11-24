class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:

            if token not in ["*"  , "+" , "-" , "/"]:

                stack.append(int(token))

            else:

                left = stack.pop()

                right = stack.pop()


                if token in "+":

                    result = right + left

                elif token in "-":

                    result = right - left

                elif token in "/":
                    result = int(right / left)

                elif token in "*":

                    result = right * left

                stack.append(result)
            
        return stack.pop()

                






        