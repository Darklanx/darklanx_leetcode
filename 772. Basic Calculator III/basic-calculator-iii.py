class Solution:
    def calculate(self, s: str) -> int:
        def is_operator(ch):
            return ch == '+' or ch =='-' or ch == '/' or ch == '*'
        
        def is_mul_div(ch):
            return ch == '*' or ch == '/'
        
        def operate(num_l, num_r, operator):
            if operator == '*':
                return num_l * num_r
            elif operator == '/':
                return int(num_l / num_r)
            elif operator == '+':
                return num_l + num_r
            elif operator == '-':
                return num_l - num_r

        
        def operate_top3(stack):
            num_r = stack.pop()
            operator = stack.pop()
            num_l = stack.pop()
            stack.append(operate(num_l, num_r, operator))
            
        def add_num(stack, num, operate_all):
            num_r = num
            while stack and is_operator(stack[-1]):
                if is_mul_div(stack[-1]) or operate_all:
                    operator = stack.pop()
                    num_l = stack.pop()
                    num_r = operate(num_l, num_r, operator)
                else:
                    break
            stack.append(int(num_r))
            
        stack = []
        s_i = 0
        while s_i < len(s):
            if s[s_i].isdigit():
                num_s = []
                while s_i < len(s) and s[s_i].isdigit():
                    num_s.append(s[s_i])
                    s_i += 1
                num = int(''.join(num_s))
                operate_all = False
                if s_i == len(s) or not is_mul_div(s[s_i]):
                    # if this is the last num or next operator is not */
                    operate_all = True
                add_num(stack, num, operate_all)
   
            elif s[s_i] == ')':
                while stack[-2] != '(':
                    num = operate_top3(stack)
                num = stack.pop()
                stack.pop() # pop '('
                operate_all = False
                if s_i+1 == len(s) or not is_mul_div(s[s_i+1]):
                    # if this is the last num or next operator is not */
                    operate_all = True
                add_num(stack, num, operate_all)
                s_i += 1
            else:
                # operator or '('
                stack.append(s[s_i])
                s_i += 1
                
        while len(stack) > 1:
            operate_top3(stack)
        return stack[0]
                