class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            a, b = b, a
            
        min_n_digits = len(b)
        new_str_list = deque()
        carry_over = 0
        for i in range(1, len(a) + 1):
            a_digit = a[-i]
            b_digit = b[-i] if len(b) - i >= 0 else '0'
            num = int(a_digit) + int(b_digit) + int(carry_over)       
            new_str_list.appendleft(str(num%2))
            carry_over = int(num >= 2)
            
        if carry_over:
            new_str_list.appendleft('1')
        return "".join(new_str_list)
            