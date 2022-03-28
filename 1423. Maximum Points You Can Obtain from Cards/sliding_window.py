class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
    max_score = cur_score = sum(cardPoints[:k])
    for i in range(1, k + 1):
        cur_score += cardPoints[-i] - cardPoints[k-i]  # right_side - left_side
        max_score = max(cur_score, max_score)
    return max_score