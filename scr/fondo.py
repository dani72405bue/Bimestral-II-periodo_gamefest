import os
import pygame
from settings import IMAGE_DIR, SCREEN_WIDTH, SCREEN_HEIGHT

class Fondo:
    def __init__(self):
        path = os.path.join(IMAGE_DIR, "fondo.png")
        self.image = pygame.image.load(path).convert()
        self.image = pygame.transform.scale(self.image, (SCREEN_WIDTH, SCREEN_HEIGHT))
        self.x = 0
        self.speed = 2

    def update(self):
        self.x -= self.speed
        if self.x <= -SCREEN_WIDTH:
            self.x = 0

    def draw(self, screen):
        screen.blit(self.image, (self.x, 0))
        screen.blit(self.image, (self.x + SCREEN_WIDTH, 0))
