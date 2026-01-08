from globals import *
import pygame

#making obstacles in map.  not dynaic, static

OBSTACLES = [
    pygame.Rect(LEFT_GUTTER + 170, 150, 20, 250),
    pygame.Rect(LEFT_GUTTER + 420, 500, 20, 300),
    pygame.Rect(LEFT_GUTTER + 500, 10, 20, 250),
    pygame.Rect(LEFT_GUTTER + 700, 350, 20, 250),
    pygame.Rect(LEFT_GUTTER + 900, 100, 20, 250),
    pygame.Rect(LEFT_GUTTER + 920, 550, 20, 250),
    pygame.Rect(LEFT_GUTTER + 300, 350, 250, 20),
    pygame.Rect(LEFT_GUTTER + 100, 650, 320, 20),
]

def point_to_grid(p):
    return (
        int((p[0] - MARGIN) // GRID_SIZE),
        int((p[1] - MARGIN) // GRID_SIZE)
    )

def grid_to_point(g):
    return (
        MARGIN + g[0]*GRID_SIZE + GRID_SIZE//2,
        MARGIN + g[1]*GRID_SIZE + GRID_SIZE//2
    )

def is_blocked(gx, gy):
    px, py = grid_to_point((gx, gy))
    return any(obs.collidepoint(px, py) for obs in OBSTACLES)

def clamp_to_free_cell(g):
    if not g:
        return None
    if not is_blocked(*g):
        return g
    for r in range(1, 6):
        for dx in range(-r, r+1):
            for dy in range(-r, r+1):
                nx, ny = g[0]+dx, g[1]+dy
                if 0 <= nx < GRID_W and 0 <= ny < GRID_H:
                    if not is_blocked(nx, ny):
                        return (nx, ny)
    return None

def estimate_path_cost(start_pos, goal_pos):
    start = clamp_to_free_cell(point_to_grid(start_pos))
    goal  = clamp_to_free_cell(point_to_grid(goal_pos))
    if not start or not goal:
        return None
    from planning.astar import astar
    path = astar(start, goal)
    if not path:
        return None
    return len(path) * GRID_SIZE
