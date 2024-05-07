from utils import draw_circle
import time

GREEN_ON = (0, 255, 0)
YELLOW_ON = (255, 255, 0)
RED_ON = (255, 0, 0)
GREEN_OFF = (38, 105, 38)
YELLOW_OFF = (115, 115, 40)
RED_OFF = (102, 39, 39)

STATE_COLORS = {
    'green': {'green': GREEN_ON, 'yellow': YELLOW_OFF, 'red': RED_OFF},
    'yellow': {'green': GREEN_OFF, 'yellow': YELLOW_ON, 'red': RED_OFF},
    'red': {'green': GREEN_OFF, 'yellow': YELLOW_OFF, 'red': RED_ON}
}

STATE_TIMINGS = {
    'green': 5,  # 5 seconds for green light
    'yellow': 2,  # 2 seconds for yellow light
    'red': 3  # 3 seconds for red light
}

class StopLight:
    def __init__(self, x, y, radius):
        self.state = 'green'
        self.x = x
        self.y = y
        self.radius = radius
        self.start_time = time.time()

    def advance_state(self):
        if self.state == 'green':
            self.state = 'yellow'
        elif self.state == 'yellow':
            self.state = 'red'
        elif self.state == 'red':
            self.state = 'green'
        else:
            raise ValueError(f"Invalid state: {self.state}")
        self.start_time = time.time()

    def get_light_colors(self):
        try:
            return STATE_COLORS[self.state]
        except KeyError:
            raise ValueError(f"Invalid state: {self.state}")

    def draw(self, screen):
        colors = self.get_light_colors()
        draw_circle(screen, self.x, self.y - self.radius * 2, self.radius, colors['green'])
        draw_circle(screen, self.x, self.y, self.radius, colors['yellow'])
        draw_circle(screen, self.x, self.y + self.radius * 2, self.radius, colors['red'])

        elapsed_time = time.time() - self.start_time
        if elapsed_time >= STATE_TIMINGS[self.state]:
            self.advance_state()
