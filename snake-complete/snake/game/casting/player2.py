import constants
from game.casting.actor import Actor
from game.casting.snake import Snake
from game.shared.point import Point

class Player2(Snake):
    def __init__(self):
        super().__init__()
    def get_segments(self):
        return self._segments

    def move_next(self):
        super().move_next()

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):
        super().grow_tail(number_of_segments, color)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)
    
    def _prepare_body(self):
        x = int(constants.MAX_X / 2)+int(constants.MAX_X / 4)
        y = int(constants.MAX_Y / 2)

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = "8" if i == 0 else "#"
            color = constants.YELLOW if i == 0 else constants.BLUE
            
            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
