import pygame
import sys
from constants import *
from logger import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0

    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # --- Crear grupos ---
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group() 
    shots = pygame.sprite.Group()

    # --- Asignar contenedores a la clase Player ---
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, drawable, updatable)
    AsteroidField.containers = (updatable,)
    Shot.containers = (shots, drawable, updatable)

    asteroid_field = AsteroidField()

    # --- Crear la instancia del jugador ---
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    # --- Game loop ---
    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        # Actualizar todos los objetos del grupo "updatable"
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

        # Dibujar todos los objetos del grupo "drawable"
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limitar FPS y calcular delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()