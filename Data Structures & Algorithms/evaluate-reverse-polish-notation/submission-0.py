class Solution:
    def evalRPN(self, tokens: List[str]) -> int:


        stack = []

        for token in tokens:


            if token not in ["+", "-" ,"*" ,"/"]:

                stack.append(int(token))

            else:

                right = stack.pop()

                left = stack.pop()


                if token in "+":
                    result = left + right

                elif token in "*":
                    result = left * right

                elif token in "-":
                    result = left - right

                elif token in "/":
                    result = int(left / right)

                
                stack.append(result)


        return stack.pop()





        