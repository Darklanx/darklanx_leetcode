from collections import namedtuple
Folder = namedtuple('Folder',["name", "level"])
class Solution:
    def lengthLongestPath(self, input: str) -> int:
        def is_folder(item):
            return item.find('.') == -1
        max_abs_path = 0
        items = input.split("\n")
        stack = [Folder("dummy", -1)]

        for item in items:
            
            level = item.count('\t')
            while stack:
                top = stack[-1]
                if level != top.level + 1:
                    stack.pop()
                else:
                    break

            stack.append(Folder(item, level))
            
            if not is_folder(item):
                cur_folder_path = ''.join(map(lambda item: item[0].strip('\t'), stack[1:]))
                cur_len = len(cur_folder_path) + len('/')*(len(stack[1:]) - 1)
                max_abs_path = max(max_abs_path, cur_len)
                stack.pop()

        return max_abs_path
                                   
                                   
            