#
# @lc app=leetcode id=818 lang=python3
#
# [818] Race Car
#

# @lc code=start

'''
BFS solution
Notes:
1. Remember to add pruning when solving problems with BFS

'''
from collections import deque, namedtuple
from multiprocessing.sharedctypes import Value
from unicodedata import name
import numpy as np
State = namedtuple("State", "pos speed steps")
class Solution:
    def racecar(self, target: int) -> int:
        def move(state: namedtuple, operation: str) -> State:
            if operation == 0:
                return State(state.pos + state.speed, state.speed * 2, state.steps + 1)
            elif operation == 1:
                return State(state.pos, np.sign(state.speed) * -1, state.steps + 1)
            else:
                raise ValueError("Unknown operation")

        states = deque()
        states.append(State(0, 1, 0))
        added_states = set((states[0].pos, states[0].speed))
        while True:
            if len(states) == 0:
                return -1 # no solution
            current_state = states[0]
            if current_state.pos == target:
                return current_state.steps
            states.popleft()
            for op in [0, 1]:
                new_state = move(current_state, op)
                if new_state.pos >= 0 and ((new_state.pos, new_state.speed) not in added_states):
                    if abs(new_state.speed) <= 2 * target and abs(new_state.pos) <= 2 * target:
                        states.append(new_state)
                        added_states.add((new_state.pos, new_state.speed))           
# @lc code=end

