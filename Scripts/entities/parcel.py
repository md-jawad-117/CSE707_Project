import time
import pygame
from config import PARCEL_COLOR

class Parcel:
    _id = 0

    def __init__(self, src_box, target_id):
        self.id = Parcel._id
        Parcel._id += 1

        self.source = src_box
        self.target_id = target_id
        self.position = src_box.rect.center

        self.spawn_time = time.time()
        self.assign_time = None
        self.delivery_time = None

        self.status = "ANNOUNCED"
        self.bids = {}
        self.auction_start = time.time()
        self.carrier_id = None

    def receive_bid(self, robot_id, cost):
        self.bids[robot_id] = cost

    def close_auction(self, robots, out_boxes, timeout=0.5):
        if time.time() - self.auction_start < timeout or not self.bids:
            return
        winner = min(self.bids, key=self.bids.get)
        robots[winner].assign(self, out_boxes)

    def draw(self, screen):
        if self.status in ("ANNOUNCED", "ASSIGNED"):
            pygame.draw.circle(screen, PARCEL_COLOR, self.position, 6)
