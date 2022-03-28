'''
By sorting with enqueueTime
if tasks[i+1] is available, tasks[i] must also be available
1. Determine what are the available tasks
2. Select the task with minimum processing time among available tasks 
3. process the task and goto (1)
'''
from collections import namedtuple
TimeId = namedtuple("TimeId", ["time", "id"])
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = [(task[0], task[1], idx) for idx, task in enumerate(tasks)]
        tasks.sort()
        min_time_heap = []
        fin_task_ids = []
        enque_id = 0 
        cur_time = 1
        while enque_id < len(tasks) or min_time_heap:

            while enque_id < len(tasks) and tasks[enque_id][0] <= cur_time:
                heapq.heappush(min_time_heap, TimeId(tasks[enque_id][1], tasks[enque_id][2]))
                enque_id += 1
                
            if min_time_heap:
                time, idx = heapq.heappop(min_time_heap)
                cur_time += time
                fin_task_ids.append(idx)
            else:
                # if theres job left in the queue but cpu is idle
                cur_time = tasks[enque_id][0]
            
            
        return fin_task_ids
        