import pygame
from config import *
from entities.box import Box
from globals import LEFT_GUTTER, WORLD_WIDTH

#parcel in and parcel out box making

def create_vertical_boxes(x, box_type, color):
    boxes = []
    spacing = (SCREEN_HEIGHT - 2 * MARGIN) / NUM_BOXES_PER_SIDE

    for i in range(NUM_BOXES_PER_SIDE):
        y = MARGIN + i * spacing + spacing / 2 - BOX_HEIGHT / 2
        rect = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)
        boxes.append(Box(i, box_type, rect, color))

    return boxes


def create_horizontal_boxes(y, box_type, color):
    boxes = []
    spacing = WORLD_WIDTH / NUM_BOXES_PER_SIDE

    for i in range(NUM_BOXES_PER_SIDE):
        x = LEFT_GUTTER + i * spacing + spacing / 2 - BOX_WIDTH / 2
        rect = pygame.Rect(x, y, BOX_WIDTH, BOX_HEIGHT)
        boxes.append(Box(i, box_type, rect, color))

    return boxes
