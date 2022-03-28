'''
whenever we count (x, y)
we loop all points[i] where points[i].x == x
compute diff= abs(points[i].y - y)
=> (x, y) (x, p1.y)
check
1. (x+diff, y) and (x+diff, p1.y)
2. (x-diff, y) and (x-diff, p1.y)

(11, 10) => (3, 10), (3, 2), (19, 10), (19, 2)
(3, 2)
(3, 10)
(11, 2)
'''

class DetectSquares:

    def __init__(self):
        self.xs = defaultdict(lambda: defaultdict(lambda : 0))
        # self.ys = defaultdict(lambda: defaultdict(lambda : 0))

    def add(self, point: List[int]) -> None:
        x, y = point
        self.xs[x][y] += 1

    def count(self, point: List[int]) -> int:
        x1, y1 = point
        n_count = 0
        # (x1, y1) (x1, y2) (x1 +- diff, y1), (x1 +- diff, y2)
        for y2 in self.xs[x1].keys():
            if y1 == y2:
                continue
            diff = abs(y1-y2)
            n_count += self.xs[x1][y2] * self.xs[x1-diff][y2] * self.xs[x1-diff][y1]
            n_count += self.xs[x1][y2] * self.xs[x1+diff][y2] * self.xs[x1+diff][y1]
        return n_count
            
        


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)