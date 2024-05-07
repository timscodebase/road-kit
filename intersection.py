from typing import List
from road import Road

class Intersection:
  def __init__(self, x, y, roads: List[Road]):
    self.x = x
    self.y = y
    self.roads = roads
  
  def draw(self, screen):
    
