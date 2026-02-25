import pygame
from constants import *
from logger import log_state
from player import Player

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

    # --- Asignar contenedores a la clase Player ---
    Player.containers = (updatable, drawable)

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

        # Dibujar todos los objetos del grupo "drawable"
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        # Limitar FPS y calcular delta time
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()