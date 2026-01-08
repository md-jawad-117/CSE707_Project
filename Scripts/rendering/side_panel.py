import pygame
from config import BLACK, SCREEN_HEIGHT, SCREEN_WIDTH, SIDE_PANEL_WIDTH

#the panel which tells about robot and package state

def draw_side_panel(screen, font, robots, parcels):
    panel_x = SCREEN_WIDTH - SIDE_PANEL_WIDTH
    pygame.draw.rect(
        screen,
        (235, 235, 235),
        (panel_x, 0, SIDE_PANEL_WIDTH, SCREEN_HEIGHT)
    )

    y = 20
    screen.blit(font.render("ROBOT STATUS", True, BLACK), (panel_x + 10, y))
    y += 30

    for r in robots:
        status = f"R{r.id} | E:{int(r.energy)} | {r.state}"
        if r.parcel:
            status += f" IN_{r.parcel.source.id} → OUT_{r.parcel.target_id}"
        else:
            status += " NONE"

        screen.blit(font.render(status, True, BLACK), (panel_x + 10, y))
        y += 22

    y += 20
    screen.blit(font.render("PARCELS", True, BLACK), (panel_x + 10, y))
    y += 30

    for p in parcels:
        rid = p.carrier_id if p.carrier_id is not None else "-"
        txt = f"P{p.id} [{p.status}] IN_{p.source.id}{p.source.side} → OUT_{p.target_id} | R{rid}"
        screen.blit(font.render(txt, True, BLACK), (panel_x + 10, y))
        y += 20
