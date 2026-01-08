import heapq
from planning.grid_utils import is_blocked
from globals import GRID_W, GRID_H


# A* shortest path algorithm defining

def astar(start, goal):
    open_set = [(0, start)]
    came_from = {}
    g = {start: 0}

    def h(a, b):
        return abs(a[0]-b[0]) + abs(a[1]-b[1])

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            return path[::-1]

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = current[0]+dx, current[1]+dy
            if not (0 <= nx < GRID_W and 0 <= ny < GRID_H):
                continue
            if is_blocked(nx, ny):
                continue

            tentative = g[current] + 1
            if tentative < g.get((nx, ny), 1e9):
                came_from[(nx, ny)] = current
                g[(nx, ny)] = tentative
                heapq.heappush(open_set, (tentative + h((nx, ny), goal), (nx, ny)))
    return None
