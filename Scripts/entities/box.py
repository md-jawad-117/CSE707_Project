import pygame
from config import BLACK

class Box:
    def __init__(self, box_id, box_type, rect, color):
        self.id = box_id
        self.type = box_type
        self.rect = rect
        self.color = color
        self.side = None

    def draw(self, screen, font):
        pygame.draw.rect(screen, self.color, self.rect)
        pygame.draw.rect(screen, BLACK, self.rect, 2)
        label = font.render(f"{self.type}_{self.id}", True, BLACK)
        screen.blit(label, (self.rect.left + 6, self.rect.centery - 8))
