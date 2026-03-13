from circleshape import CircleShape
from constants import *
import pygame
import random
from logger import log_event

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        log_event("asteroid_split")

        # ángulo aleatorio
        angle = random.uniform(20, 50)

        # nuevos vectores de dirección
        v1 = self.velocity.rotate(angle)
        v2 = self.velocity.rotate(-angle)

        # nuevo radio
        new_radius = self.radius - ASTEROID_MIN_RADIUS

        # crear nuevos asteroides
        asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)

        # asignar velocidad (1.2x más rápido)
        asteroid1.velocity = v1 * 1.2
        asteroid2.velocity = v2 * 1.2