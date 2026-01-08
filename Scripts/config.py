import pygame
import os

# all variable and stuff

EXPERIMENT_NAME = "load_penalty_ablation"
LOAD_PENALTY = 80    # if a robot has many assigned task then encourses less work robot to pick that parcel

LOG_DIR = "E:/MSC_University Academics/Fall 2025/CSE707/Project/COde"        # Change FIle path here please based on ur pc
os.makedirs(LOG_DIR, exist_ok=True)

CSV_PATH = os.path.join(
    LOG_DIR,
    f"{EXPERIMENT_NAME}_LOAD_{int(LOAD_PENALTY)}.csv"
)

# screen display metrics, code simulation might look weird in differetn resoltuion screen 

SIDE_PANEL_WIDTH = 300
SCREEN_HEIGHT = 900
SCREEN_WIDTH = 1300 + SIDE_PANEL_WIDTH
FPS = 60


# siu env setup

GRID_SIZE = 15
MARGIN = 10
BOX_WIDTH = 90
BOX_HEIGHT = 40
NUM_BOXES_PER_SIDE = 4

# robot infor
NUM_ROBOTS = 15
ROBOT_RADIUS = 10
ROBOT_SPEED = 2

MAX_ENERGY = 1000
ENERGY_COST_PER_PIXEL = 0.5
CHARGE_RATE = 120
HOME_RADIUS = 12

# 

PARCEL_INTERVAL = 2.5
ASSIGN_TIMEOUT = 6

# interfce color

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
IN_BOX_COLOR = (100, 180, 255)
OUT_BOX_COLOR = (120, 220, 140)
ROBOT_COLOR = (60, 60, 60)
PARCEL_COLOR = (220, 120, 120)
CENTER_BORDER = (170, 170, 170)
PATH_COLOR = (180, 180, 255)
