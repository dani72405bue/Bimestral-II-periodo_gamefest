import os
import pygame
from settings import IMAGE_DIR, GROUND_Y, JUMP_SPEED, GRAVITY

class Personaje:
    def __init__(self):
        path = os.path.join(IMAGE_DIR, "personaje.png")
        self.image = pygame.image.load(path).convert_alpha()
        self.rect = self.image.get_rect(midbottom=(140, GROUND_Y))
        self.vel_y = 0
        self.is_jumping = False

    def jump(self):
        if not self.is_jumping:
            self.vel_y = JUMP_SPEED
            self.is_jumping = True

    def update(self):
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        if self.rect.bottom >= GROUND_Y:
            self.rect.bottom = GROUND_Y
            self.vel_y = 0
            self.is_jumping = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)
