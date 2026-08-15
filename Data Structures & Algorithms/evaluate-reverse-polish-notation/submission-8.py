class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops_list = ["+", "-", "*", "/"]
        stack = []
        for i in tokens:
            if i not in ops_list:
                stack.append(int(float(i)))
            else:
                a, b = stack.pop(), stack.pop()
                if i == "+":
                    v = a+b
                elif i == "-":
                    v = b-a
                elif i == "*":
                    v = a*b
                else:
                    v = int(b/a)
                stack.append(v)

        return stack.pop()
