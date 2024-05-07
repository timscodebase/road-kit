import pygame
from contextlib import contextmanager
from constants import WIDTH, HEIGHT
from stop_light import StopLight
from road import Road

@contextmanager
def pygame_context():
    pygame.init()
    try:
        yield
    finally:
        pygame.quit()

with pygame_context():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Stop Light")
    clock = pygame.time.Clock()

    stop_light_1 = StopLight(150, 200, 50)
    stop_light_2 = StopLight(250, 200, 50)
    stop_light_3 = StopLight(150, 600, 50)
    stop_light_4 = StopLight(250, 600, 50)
    road_1 = Road(0, 0, [stop_light_1, stop_light_2])
    road_2 = Road(200, 0, [stop_light_3, stop_light_4])

    running = True
    while running:
        clock.tick(60)  # Limit the frame rate

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop_light_1.advance_state()

        screen.fill((0, 0, 0))  # Clear the screen
        road_1.draw(screen)  # Draw the stop light
        road_2.draw(screen)
        pygame.display.flip()  # Update the display