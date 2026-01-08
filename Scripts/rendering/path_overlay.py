import pygame

# the line that follow when robots move, helps better visuliaztion.  Blue line means going to pick parcel, green means sending parcel to destination, none means returning

def draw_paths(screen, robots, width, height): 
    path_layer = pygame.Surface((width, height), pygame.SRCALPHA)

    for r in robots:
        if not r.path or r.path_index >= len(r.path):
            continue
        if r.state == "IDLE":
            continue

        MAX_PATH_DRAW = 8
        remaining = r.path[r.path_index : r.path_index + MAX_PATH_DRAW]
        if len(remaining) < 2:
            continue

        if r.state == "TO_IN":
            color = (120, 120, 255, 150)
        elif r.state == "TO_OUT":
            color = (120, 200, 120, 150)
        else:
            continue

        pygame.draw.lines(path_layer, color, False, remaining, 4)

    screen.blit(path_layer, (0, 0))
