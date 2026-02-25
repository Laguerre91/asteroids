import pygame
from circleshape import CircleShape
from constants import *

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, radius=PLAYER_RADIUS)
        self.rotation = 0
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), LINE_WIDTH)

    def update(self, dt):
        # Update player position based on velocity
        self.position += self.velocity * dt
    
    # in the Player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)        # mover hacia adelante
        if keys[pygame.K_s]:
            self.move(-dt)   

    def move(self, dt):
        # Crear vector unitario apuntando "hacia abajo"
        unit_vector = pygame.Vector2(0, 1)

        # Rotar para que apunte en la dirección del jugador
        rotated_vector = unit_vector.rotate(self.rotation)

        # Escalar por velocidad y delta time
        rotated_with_speed_vector = rotated_vector * PLAYER_SPEED * dt

        # Mover al jugador
        self.position += rotated_with_speed_vector
            