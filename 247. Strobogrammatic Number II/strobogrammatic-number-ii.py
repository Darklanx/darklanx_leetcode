'''
0 : 0
1 : 1
6 : 9
8 : 8
9 : 6

1 + "" + 1
6 + "" + 9
'''
class Solution:
    def findStrobogrammatic(self, n: int, first: bool = True) -> List[str]:
        counter_parts = {"0":"0", "1":"1", "6":"9", "8":"8", "9":"6"}
        single_counter_parts = {"0":"0", "1":"0", "8":"0"}
        if n == 0:
            return [""]
        if n == 1:
            return [str(num) for num in single_counter_parts.keys()]
        
        all_strob = []
        for num, counter_num in counter_parts.items():
            if first and num == "0":
                continue
            for sub in self.findStrobogrammatic(n-2, False):
                all_strob.append(num + sub + counter_num)
            
        return all_strob