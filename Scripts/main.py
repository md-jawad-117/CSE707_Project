from config import *
from globals import *
from entities import Box, Parcel, Robot
from rendering import draw_side_panel, draw_paths
from planning.grid_utils import OBSTACLES
from experiment import ExperimentLogger
import pygame, random, time, sys
from helpers import create_vertical_boxes, create_horizontal_boxes


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 16, bold=True)

    logger = ExperimentLogger()

    #  box for parcel in(Blue) and Parcel Out (Green) 
    from helpers import create_vertical_boxes, create_horizontal_boxes
    left = create_vertical_boxes(MARGIN, "IN", IN_BOX_COLOR)
    right = create_vertical_boxes(LEFT_GUTTER + WORLD_WIDTH - BOX_WIDTH - MARGIN, "IN", IN_BOX_COLOR)
    for b in left: b.side = "L"
    for b in right: b.side = "R"
    in_boxes = left + right
    out_boxes = create_horizontal_boxes(MARGIN, "OUT", OUT_BOX_COLOR)

    # === robot charge deport,, position here root return after work done ===
    depot_x = LEFT_GUTTER + WORLD_WIDTH // 2
    depot_y = SCREEN_HEIGHT // 2 - 100

    robots = [Robot(i, (depot_x, depot_y + i*25)) for i in range(NUM_ROBOTS)]
    parcels = []
    last_spawn = time.time()

    running = True
    try:
        while running:
            clock.tick(FPS)
            now = time.time()

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    running = False

            if now - last_spawn > PARCEL_INTERVAL:
                src = random.choice(in_boxes)
                parcels.append(Parcel(src, random.randint(0, NUM_BOXES_PER_SIDE-1)))
                last_spawn = now

            for p in parcels:
                if p.status == "ANNOUNCED":
                    for r in robots:
                        bid = r.compute_bid(p)
                        if bid is not None:
                            p.receive_bid(r.id, bid)
                    p.close_auction(robots, out_boxes)

            screen.fill(WHITE)
            for obs in OBSTACLES:
                pygame.draw.rect(screen, (90,90,90), obs)
                pygame.draw.rect(screen, (0,0,0), obs, 2)

            for b in in_boxes + out_boxes:
                b.draw(screen, font)

            draw_paths(screen, robots, SCREEN_WIDTH, SCREEN_HEIGHT)

            for r in robots:
                r.update()
                r.draw(screen, font)

            # log + remove delivered parcels form side bar
            delivered = [p for p in parcels if p.status == "DELIVERED"]
            for p in delivered:
                logger.log(p, robots[p.carrier_id])
            parcels = [p for p in parcels if p.status != "DELIVERED"]

            #
            for p in parcels:
                p.draw(screen)

            draw_side_panel(screen, font, robots, parcels)

            pygame.display.flip()

    finally:
        logger.close()
        pygame.quit()


if __name__ == "__main__":
    main()
