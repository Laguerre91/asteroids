from circleshape import CircleShape
from constants import *
import pygame

class Shot(CircleShape):
    def __init__(self, x, y, rotation):
        super().__init__(x, y, SHOT_RADIUS)
        self.rotation = rotation
        self.speed = 400

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius)

    def update(self, dt):
        unit_vector = pygame.Vector2(0, 1)

        rotated_vector = unit_vector.rotate(self.rotation)

        rotated_with_speed_vector = rotated_vector * self.speed * dt

        self.position += rotated_with_speed_vector