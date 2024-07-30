from typing import List

class Solution:
    def findPath(self, m: List[List[int]]) -> List[str]:
        # length of m
        n = len(m)

        # check if source and destination is 0 and return -1
        if m[0][0] == 0 or m[n - 1][n - 1] == 0:
            return []
        # create a variable for directions
        possibleDirections = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
        # create a variable for paths
        paths = []

        # create a variable for visited
        visited = [[False] * n for _ in range(n)]

        def isSafe(x, y):
            return 0 <= x < n and 0 <= y < n and m[x][y] == 1 and not visited[x][y]

        def ratMove(x, y, path):
            if x == n - 1 and y == n - 1:
                paths.append(path)
                return
            visited[x][y] = True
            for direction, (dx, dy) in possibleDirections.items():
                newX, newY = (x + dx, y + dy)
                if isSafe(newX, newY):
                    ratMove(newX, newY, path + direction)

            visited[x][y] = False

        # code here
        ratMove(0, 0, "")
        return sorted(paths) if paths else []
