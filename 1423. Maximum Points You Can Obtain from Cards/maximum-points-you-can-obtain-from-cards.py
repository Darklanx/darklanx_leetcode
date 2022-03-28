'''
since we can only take cards from the leftmost/rightmost position
if we can take `k` cards, following are the choices:

left: 0,    right: k
left: 1,    right: k-1
.
.
.
left: k-1,  right:1
left: k,    right: 0

1 2 3 4 5 6 1
0 1 3 6 10 15 21 22
22 21 19 16 12 7 1 0
'''
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        left_sum = [0 for i in range(n+1)]
        right_sum = [0 for i in range(n+1)]
        for i in range(1, n+1):
            left_sum[i] = cardPoints[i-1] + left_sum[i-1]
        for i in reversed(range(n)):
            right_sum[i] = cardPoints[i] + right_sum[i+1]
        _max = -math.inf
        for i in range(k+1):
            _max = max(_max, left_sum[i] + right_sum[-k-1 + i])
        return _max
            
        