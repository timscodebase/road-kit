import pygame
from constants import WIDTH, HEIGHT
from stop_light import StopLight
from typing import List

class Road:
  def __init__(self, x: int, y: int, stop_lights: List[StopLight]):
    self.x = x
    self.y = y
    self.stop_lights = stop_lights
    self.stop_light_states = [stop_light.state for stop_light in self.stop_lights]

  def __repr__(self):
    return f"({self.stop_lights_states})"
  
  def draw_road(self, screen) -> None:
        pygame.draw.rect(screen, (0, 0, 0), (self.x, self.y, WIDTH, HEIGHT))

  def draw_stop_lights(self, screen) -> None:
      for stop_light in self.stop_lights:
          stop_light.draw(screen)

  def draw(self, screen) -> None:
      self.draw_road(screen)
      self.draw_stop_lights(screen)