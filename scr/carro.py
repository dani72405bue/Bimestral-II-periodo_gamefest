import os
import random
import pygame
from settings import IMAGE_DIR, SCREEN_WIDTH, GROUND_Y, START_SPEED

class Carro:
    def __init__(self, x_position):
        path = os.path.join(IMAGE_DIR, "obstaculo.png")
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(x_position, GROUND_Y))
        self.speed = START_SPEED

    def update(self, speed):
        self.rect.x -= speed
        if self.rect.right < 0:
            self.reset()

    def reset(self):
        self.rect.left = SCREEN_WIDTH + random.randint(120, 420)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
