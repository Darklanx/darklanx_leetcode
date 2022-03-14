'''
 H1 H2 : M1 M2
 => 4! = 24 combination  + 4
  23 >= H1 H2 >= 00
  59 >= M1M2  >= 00
  
 1. keep only unique
 2. generate all combination + duplicate number
 3. sort all combination
 4. try same hour, next minute
 5. try next hour, min minute
 6. try min hour, min minute
'''

class Solution:
    def nextClosestTime(self, time: str) -> str:
        def get_next(nums, base, _max):
            for num in nums:
                if num > _max:
                    break
                    
                if num > base:
                    return num
                
            return None

        
        hr = int(time[0:2])
        minute = int(time[3:])
        unique_ch = set(time)
        unique_ch.remove(":")
        nums = []
        for ch1 in unique_ch:
            for ch2 in unique_ch:
                new_str = ch1 + ch2
                if int(new_str) < 60:
                    nums.append(int(new_str))
        nums.sort()
        # assume same hour
        new_hr = hr
        new_minute = get_next(nums, minute, 59)
        if new_minute is None:
            # get next hour and min minute
            new_hr = get_next(nums, hr, 23)
            if new_hr is not None:
                new_minute = nums[0]
            else:
                # get_next day
                new_hr = new_minute = nums[0]


        return str(new_hr).zfill(2) + ":" + str(new_minute).zfill(2)
            
                
        