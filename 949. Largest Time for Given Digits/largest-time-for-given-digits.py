class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        len_arr = len(arr)
        max_date_num = -1
        max_date_str = ""
        for h1 in range(len_arr):
            for h2 in range(len_arr):
                for m1 in range(len_arr):
                    for m2 in range(len_arr):
                        if h1 == h2 or h1 == m1 or h1 == m2 or h2 == m1 or h2 == m2 or m1 == m2:
                            continue
                            
                        if arr[h1]*10 + arr[h2] >= 24:
                            continue
                        if arr[m1]*10 + arr[m2] >= 60:
                            continue
                            
                        new_max_date_num = arr[h1]*1000 + arr[h2]*100 + arr[m1]*10 + arr[m2]
                        
                        if new_max_date_num > max_date_num:
                            max_date_num = new_max_date_num
                            max_date_str = str(arr[h1]) + str(arr[h2]) + ":" + str(arr[m1]) + str(arr[m2])

        return max_date_str
