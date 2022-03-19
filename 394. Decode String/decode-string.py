from collections import deque
class Solution:

    def decodeString(self, s: str) -> str:
        def get_string(stack):
            string = deque()
            while stack and stack[-1] != '[':
                string.appendleft(stack.pop())
            stack.pop() # '['
            return "".join(string)

        
        def is_number(ch):
            if len(ch) > 1:
                return False
            return ord(ch) >= ord('0') and ord(ch) <= ord('9')

        def get_num(stack):
            num_string = deque()
            while stack and is_number(stack[-1]):
                num_string.appendleft(stack.pop())

            return int("".join(num_string))


        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                tmp_str = get_string(stack)
                mul = get_num(stack)
                stack.append(mul * tmp_str)

            
        return "".join(stack)from collections import deque
class Solution:

    def decodeString(self, s: str) -> str:
        def get_string(stack):
            string = deque()
            while stack and stack[-1] != '[':
                string.appendleft(stack.pop())
            stack.pop() # '['
            return "".join(string)

        
        def is_number(ch):
            if len(ch) > 1:
                return False
            return ord(ch) >= ord('0') and ord(ch) <= ord('9')

        def get_num(stack):
            num_string = deque()
            while stack and is_number(stack[-1]):
                num_string.appendleft(stack.pop())

            return int("".join(num_string))


        stack = []
        for ch in s:
            if ch != ']':
                stack.append(ch)
            else:
                tmp_str = get_string(stack)
                mul = get_num(stack)
                stack.append(mul * tmp_str)

            
        return "".join(stack)