import pygame
from stop_light import StopLight

WIDTH, HEIGHT = 400, 600

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Stop Light")
clock = pygame.time.Clock()

# Create a stop light instance
stop_light_1 = StopLight(200, 300, 50)
stop_light_2 = StopLight(300, 300, 50)
stop_light_3 = StopLight(100, 300, 50)


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
    stop_light_1.draw(screen)  # Draw the stop light
    stop_light_2.draw(screen)
    stop_light_3.draw(screen)
    pygame.display.flip()  # Update the display

pygame.quit()