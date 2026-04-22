import math

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dists = []

        for i in range(len(points)):
            point = points[i]
            dists.append(
                (math.sqrt((point[0] ** 2) + (point[1] ** 2)), i)
            )
        
        dists.sort(key=lambda x: x[0])

        print(dists)

        return list(map(lambda x: points[x[1]], dists[:k]))