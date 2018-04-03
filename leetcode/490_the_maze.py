class Solution:
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        if not maze or not maze[0] or not start or not destination:
            return False

        x, y = start
        tx, ty = destination
        visited = set()
        return self.dfs(maze, x, y, tx, ty, visited)

    def dfs(self, maze, x, y, tx, ty, visited):
        if x == tx and y == ty:
            return True
        if (x, y) in visited:
            return False

        visited.add((x, y))

        m, n = len(maze), len(maze[0])

        for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            _x = x + dx
            _y = y + dy

            while 0 <= _x < m and 0 <= _y < n and maze[_x][_y] == 0:
                _x += dx
                _y += dy

            # since for now its means the position of wall
            _x -= dx
            _y -= dy

            if self.dfs(maze, _x, _y, tx, ty, visited):
                return True

        return False


if __name__ == '__main__':
    s = Solution()
    maze = [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]]

    for _in, _out in ((
        ((maze, [0, 4], [4, 4]), True),
        ((maze, [0, 4], [3, 2]), False),
    )):
        res = s.hasPath(*_in)

        if res == _out:
            print('[{0}]: got {1}'.format('Pass', res))
        else:
            print('[{0}]: got {1}, but expect {2}'.format('Failed', res, _out))
