import math
import pygame
import time

from config import *
from planning.astar import astar
from planning.grid_utils import (
    point_to_grid,
    grid_to_point,
    clamp_to_free_cell,
    estimate_path_cost,
)

class Robot:
    def __init__(self, rid, pos):
        self.id = rid
        self.pos = list(pos)
        self.origin = pos

        self.state = "IDLE"
        self.task_count = 0

        self.energy = MAX_ENERGY   #max battery power

        self.parcel = None
        self.out_boxes = None

        self.path = []
        self.path_index = 0
        self.target = None

    # chhecks how whihc robot is suitbale for taking task, the load penatly here determines it, 
    def compute_bid(self, parcel):
        if self.state != "IDLE":
            return None

        path_cost = estimate_path_cost(self.pos, parcel.position)
        if path_cost is None:
            return None

        load_cost = LOAD_PENALTY * self.task_count
        estimated_energy = path_cost * ENERGY_COST_PER_PIXEL * 2

        if self.energy < estimated_energy:
            return None

        return path_cost + load_cost

    # assigns parccel state
    def assign(self, parcel, out_boxes):
        self.parcel = parcel
        self.out_boxes = out_boxes

        parcel.status = "ASSIGNED"
        parcel.carrier_id = self.id
        parcel.assign_time = time.time()

        self.state = "TO_IN"
        self.task_count += 1

        start = clamp_to_free_cell(point_to_grid(self.pos))
        goal  = clamp_to_free_cell(point_to_grid(parcel.position))

        if start is None or goal is None:
            self.reset()
            return

        grid_path = astar(start, goal)
        if grid_path is None:
            self.reset()
            return

        self.path = [grid_to_point(p) for p in grid_path]
        self.path_index = 0

    def reset(self):
        self.state = "IDLE"
        self.parcel = None
        self.path = []
        self.path_index = 0

    #  robot movement calcualtion, diagonal movement avoided as in pixel based motio, it not efficient like real time
    def move(self):
        if not self.path or self.path_index >= len(self.path):
            return

        self.target = self.path[self.path_index]
        dx = self.target[0] - self.pos[0]
        dy = self.target[1] - self.pos[1]
        dist = math.hypot(dx, dy)

        if dist < 2:
            self.path_index += 1
            return

        self.pos[0] += (dx / dist) * ROBOT_SPEED
        self.pos[1] += (dy / dist) * ROBOT_SPEED
        self.energy -= ENERGY_COST_PER_PIXEL

    # update robot and parrcel stat, like what they are doing
    def update(self):
        if self.state == "IDLE":
            return

        if self.path and self.path_index >= len(self.path):

            if self.state == "TO_IN":
                self.state = "TO_OUT"
                self.parcel.status = "CARRIED"

                start = clamp_to_free_cell(point_to_grid(self.pos))
                goal = clamp_to_free_cell(
                    point_to_grid(
                        self.out_boxes[self.parcel.target_id].rect.center
                    )
                )

                grid_path = astar(start, goal)
                if grid_path is None:
                    self.reset()
                    return

                self.path = [grid_to_point(p) for p in grid_path]
                self.path_index = 0


            elif self.state == "TO_OUT":
                self.parcel.status = "DELIVERED"
                self.parcel.delivery_time = time.time()

                self.parcel = None
                self.state = "RETURN_HOME"
                self.task_count -= 1

                start = clamp_to_free_cell(point_to_grid(self.pos))
                goal  = clamp_to_free_cell(point_to_grid(self.origin))

                grid_path = astar(start, goal)
                if grid_path is None:
                    self.state = "IDLE"
                    return

                self.path = [grid_to_point(p) for p in grid_path]
                self.path_index = 0

            elif self.state == "RETURN_HOME":
                self.state = "CHARGING"
                self.path = []
                return

        self.move()

        if self.state == "CHARGING":
            self.energy += CHARGE_RATE * (1 / FPS)
            if self.energy >= MAX_ENERGY:
                self.energy = MAX_ENERGY
                self.state = "IDLE"

        if self.parcel and self.parcel.status == "CARRIED":
            self.parcel.position = tuple(self.pos)

    # robot design
    def draw(self, screen, font):
        color = ROBOT_COLOR
        if self.state == "CHARGING":
            color = (80, 160, 80)

        pygame.draw.circle(screen, color, self.pos, ROBOT_RADIUS)
        pygame.draw.circle(screen, BLACK, self.pos, ROBOT_RADIUS, 2)

        label = font.render(f"R{self.id}", True, BLACK)
        screen.blit(label, (self.pos[0]-28, self.pos[1]-22))
